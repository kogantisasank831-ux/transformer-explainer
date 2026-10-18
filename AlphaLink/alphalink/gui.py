from __future__ import annotations

import argparse
import logging
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Qt, Signal
from PySide6.QtGui import QAction, QColor, QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QApplication, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox,
    QProgressBar, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
)
from .bridge import SonyBridge
from .models import Camera, Media
from .transfers import ImportResult, ReceiptStore, TransferService


class Signals(QObject):
    done = Signal(object)
    failed = Signal(str)
    progress = Signal(object, object, object)
    imported = Signal(object)


class Job(QRunnable):
    def __init__(self, call: Callable[[], Any]) -> None:
        super().__init__()
        self.call = call
        self.signals = Signals()

    def run(self) -> None:
        try:
            self.signals.done.emit(self.call())
        except Exception as exc:
            logging.getLogger(__name__).exception('Operation failed')
            self.signals.failed.emit(str(exc))


STYLE = '''
QWidget { background: #10191d; color: #e9eeea; font-size: 13px; }
QMainWindow { background: #10191d; }
QFrame#sidebar { background: #18252a; border-radius: 12px; }
QFrame#sidebar QLabel { background: transparent; }
QLabel#title { font-size: 29px; font-weight: 650; }
QLabel#brand { font-size: 23px; font-weight: 700; color: #c7e5bc; }
QLabel#muted { color: #9cacac; }
QLabel#status { color: #c7e5bc; font-weight: 600; }
QPushButton { background: #24363d; border: 1px solid #354a50; border-radius: 7px; padding: 9px 15px; }
QPushButton:hover { background: #334a50; }
QPushButton:disabled { color: #697a80; background: #1b292e; }
QPushButton#primary { background: #c3e0b4; color: #15251d; border: 0; font-weight: 650; }
QPushButton#primary:disabled { background: #374c40; color: #83958a; }
QLineEdit, QComboBox { padding: 8px; border: 1px solid #3a4b50; border-radius: 6px; background: #19272d; }
QComboBox QAbstractItemView { background: #19272d; }
QTableWidget { background: #152228; alternate-background-color: #19282e; border: 1px solid #293c42; border-radius: 9px; gridline-color: #293c42; selection-background-color: #354d48; }
QHeaderView::section { background: #203238; padding: 12px 8px; border: 0; color: #a9bbb9; }
QProgressBar { border: 0; background: #26383e; border-radius: 5px; height: 9px; text-align: center; }
QProgressBar::chunk { background: #c3e0b4; border-radius: 5px; }
QMenuBar, QMenu { background: #18252a; }
'''


def muted(text: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName('muted')
    label.setWordWrap(True)
    return label


def size_text(value: int) -> str:
    return f'{value / 1_000_000:.1f} MB' if value >= 1_000_000 else f'{value / 1000:.1f} KB'


class Window(QMainWindow):
    def __init__(self, *, demo: bool = False, data_dir: Path | None = None) -> None:
        super().__init__()
        self.demo = demo
        if demo:
            from .demo import DemoBridge
            self.bridge = DemoBridge()
        else:
            self.bridge = SonyBridge()
        support = data_dir or Path.home() / 'Library' / 'Application Support' / 'AlphaLink'
        support.mkdir(parents=True, exist_ok=True)
        self.receipts = ReceiptStore(support / 'imports.sqlite3')
        self.destination = Path.home() / 'Pictures' / ('AlphaLink Demo' if demo else 'AlphaLink')
        self.cameras: list[Camera] = []
        self.camera: Camera | None = None
        self.items: list[Media] = []
        self.results: dict[int, ImportResult] = {}
        self.busy = False
        self.stop = threading.Event()
        self.pool = QThreadPool(self)
        self.pool.setMaxThreadCount(1)
        self._job: Job | None = None
        self.setWindowTitle('AlphaLink — Wireless Camera Import' + (' [DEMO]' if demo else ''))
        self.resize(1180, 760)
        self.setMinimumSize(1020, 650)
        self._build()
        self.setStyleSheet(STYLE)
        self._state()

    def _build(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)
        outer = QHBoxLayout(root)
        outer.setContentsMargins(22, 22, 22, 22)
        outer.setSpacing(25)
        sidebar = QFrame()
        sidebar.setObjectName('sidebar')
        sidebar.setFixedWidth(250)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(21, 26, 21, 24)
        brand = QLabel('α  AlphaLink')
        brand.setObjectName('brand')
        side.addWidget(brand)
        side.addWidget(muted('CAMERA → MAC'))
        side.addSpacing(32)
        side.addWidget(QLabel('01   Connect your camera'))
        side.addWidget(muted('Join the camera’s Wi-Fi or use the same Wi-Fi network.'))
        self.camera_box = QComboBox()
        self.camera_box.setMinimumContentsLength(12)
        side.addWidget(self.camera_box)
        self.scan_button = QPushButton('Find camera')
        self.scan_button.clicked.connect(self.scan)
        side.addWidget(self.scan_button)
        self.connect_button = QPushButton('Connect')
        self.connect_button.clicked.connect(self.connect_camera)
        side.addWidget(self.connect_button)
        self.disconnect_button = QPushButton('Disconnect')
        self.disconnect_button.clicked.connect(self.disconnect)
        side.addWidget(self.disconnect_button)
        self.connection_label = muted('No camera connected')
        side.addWidget(self.connection_label)
        side.addSpacing(25)
        side.addWidget(QLabel('02   Choose where to save'))
        self.folder_label = muted(str(self.destination))
        self.folder_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        side.addWidget(self.folder_label)
        self.folder_button = QPushButton('Choose folder…')
        self.folder_button.clicked.connect(self.choose_folder)
        side.addWidget(self.folder_button)
        show = QPushButton('Open import folder')
        show.clicked.connect(self.open_folder)
        side.addWidget(show)
        side.addStretch()
        help_button = QPushButton('Camera setup guide')
        help_button.clicked.connect(self.help)
        side.addWidget(help_button)
        side.addWidget(muted('Local transfers. Original files.\nFiles stay on your camera.'))
        outer.addWidget(sidebar)
        main = QVBoxLayout()
        main.setSpacing(16)
        title = QLabel('From camera to collection.')
        title.setObjectName('title')
        main.addWidget(title)
        main.addWidget(muted('Browse your card. Pick the files you want. Import over Wi-Fi.'))
        if self.demo:
            demo = QLabel('DEMO MODE · Generated test images · No camera is connected')
            demo.setStyleSheet('color: #e7bc79; padding: 9px; background: #3a3024; border-radius: 6px;')
            main.addWidget(demo)
        self.status = QLabel('Ready when your camera is.')
        self.status.setObjectName('status')
        main.addWidget(self.status)
        tools = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText('Search filename or date…')
        self.search.textChanged.connect(self.filter_rows)
        tools.addWidget(self.search, 1)
        self.kind = QComboBox()
        self.kind.addItems(['All files', 'Photo', 'RAW', 'Video', 'Other'])
        self.kind.currentTextChanged.connect(self.filter_rows)
        tools.addWidget(self.kind)
        self.refresh_button = QPushButton('Refresh card')
        self.refresh_button.clicked.connect(self.refresh)
        tools.addWidget(self.refresh_button)
        main.addLayout(tools)
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['Import', 'File', 'Captured', 'Size', 'Status'])
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().hide()
        self.table.setShowGrid(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.setColumnWidth(0, 65)
        self.table.setColumnWidth(3, 95)
        self.table.setColumnWidth(4, 125)
        self.table.cellDoubleClicked.connect(self.quick_look)
        self.table.itemChanged.connect(self._state)
        main.addWidget(self.table, 1)
        row = QHBoxLayout()
        self.select_button = QPushButton('Select visible')
        self.select_button.clicked.connect(lambda: self.select_visible(True))
        row.addWidget(self.select_button)
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(lambda: self.select_visible(False))
        row.addWidget(self.clear_button)
        self.count = muted('0 files')
        row.addWidget(self.count, 1)
        self.import_button = QPushButton('Import selected')
        self.import_button.setObjectName('primary')
        self.import_button.clicked.connect(self.import_selected)
        row.addWidget(self.import_button)
        main.addLayout(row)
        self.progress = QProgressBar()
        self.progress.setRange(0, 1000)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        main.addWidget(self.progress)
        bottom = QHBoxLayout()
        self.progress_label = muted('Original JPEG, HEIF, RAW and video files exposed by the camera.')
        bottom.addWidget(self.progress_label, 1)
        self.stop_button = QPushButton('Stop after current file')
        self.stop_button.clicked.connect(self.stop_queue)
        self.stop_button.hide()
        bottom.addWidget(self.stop_button)
        main.addLayout(bottom)
        outer.addLayout(main, 1)
        help_action = QAction('Setup guide', self)
        help_action.triggered.connect(self.help)
        self.menuBar().addMenu('Help').addAction(help_action)

    def _state(self, *_: Any) -> None:
        connected = self.bridge.connected
        for button in [self.scan_button, self.connect_button, self.disconnect_button,
                       self.refresh_button, self.folder_button, self.select_button, self.clear_button]:
            button.setEnabled(not self.busy)
        self.scan_button.setEnabled(not self.busy and not connected)
        self.camera_box.setEnabled(not self.busy and not connected)
        self.connect_button.setEnabled(not self.busy and not connected and bool(self.cameras))
        self.disconnect_button.setEnabled(not self.busy and connected)
        self.refresh_button.setEnabled(not self.busy and connected)
        self.import_button.setEnabled(not self.busy and connected and bool(self.selected()))
        self.table.setEnabled(not self.busy)
        selected = self.selected()
        self.count.setText(f'{len(self.items)} files · {len(selected)} selected · {size_text(sum(i.size for i in selected))}')
        if not connected:
            self.connection_label.setText('No camera connected')

    def selected(self) -> list[Media]:
        return [item for row, item in enumerate(self.items)
                if not self.table.isRowHidden(row) and self.table.item(row, 0)
                and self.table.item(row, 0).checkState() == Qt.Checked]

    def task(self, call: Callable[[], Any], done: Callable[[Any], None]) -> None:
        self.busy = True
        job = Job(call)
        self._job = job
        job.signals.done.connect(lambda result: self._finished(done, result))
        job.signals.failed.connect(self._failed)
        self._state()
        self.pool.start(job)

    def _finished(self, done: Callable[[Any], None], result: Any) -> None:
        self.busy = False
        self.stop_button.hide()
        done(result)
        self._state()

    def _failed(self, message: str) -> None:
        self.busy = False
        self.stop_button.hide()
        self.status.setText('Operation stopped — your completed imports are saved.')
        self.progress.setRange(0, 1000)
        self._state()
        QMessageBox.warning(self, 'AlphaLink', message)

    def scan(self) -> None:
        self.status.setText('Looking for your camera on the local network…')
        def done(cameras: list[Camera]) -> None:
            self.cameras = [c for c in cameras if c.wireless]
            self.camera_box.clear()
            for c in self.cameras:
                self.camera_box.addItem(f'{c.model} · {c.ip}')
            self.status.setText('Choose your camera and connect.' if self.cameras else 'No Wi-Fi camera found. Open the setup guide and try again.')
        self.task(self.bridge.discover, done)

    def connect_camera(self) -> None:
        index = self.camera_box.currentIndex()
        if index < 0:
            return
        camera = self.cameras[index]
        self.status.setText('Checking camera authentication…')
        self.task(lambda: self.bridge.fingerprint(camera), lambda fp: self.credentials(camera, fp))

    def credentials(self, camera: Camera, fingerprint: str) -> None:
        username, password = 'admin', ''
        if camera.ssh:
            dialog = QDialog(self)
            dialog.setWindowTitle('Verify your camera')
            layout = QFormLayout(dialog)
            text = QLabel('Compare this fingerprint with Network → Access Authen. Info on your camera. Continue only if they match.')
            text.setWordWrap(True)
            text.setMaximumWidth(460)
            layout.addRow(text)
            fp_label = QLabel(fingerprint)
            fp_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            fp_label.setWordWrap(True)
            fp_label.setMaximumWidth(460)
            layout.addRow('Fingerprint', fp_label)
            user = QLineEdit('admin')
            secret = QLineEdit()
            secret.setEchoMode(QLineEdit.Password)
            layout.addRow('Camera username', user)
            layout.addRow('Camera password', secret)
            layout.addRow(muted('Credentials remain in memory for this session.'))
            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.button(QDialogButtonBox.Ok).setText('Fingerprint matches — connect')
            buttons.accepted.connect(dialog.accept)
            buttons.rejected.connect(dialog.reject)
            layout.addRow(buttons)
            if dialog.exec() != QDialog.Accepted:
                self.status.setText('Connection cancelled.')
                return
            username, password = user.text(), secret.text()
            secret.clear()
        self.status.setText('Connecting… confirm any pairing request on the camera.')
        def call() -> list[Media]:
            self.bridge.connect(camera, username, password, fingerprint)
            return self.bridge.media()
        def done(items: list[Media]) -> None:
            self.camera = camera
            self.connection_label.setText(f'{camera.model}\nWi-Fi · {camera.ip}')
            self.populate(items)
        self.task(call, done)

    def populate(self, items: list[Media]) -> None:
        self.items = sorted(items, key=lambda i: (i.captured, i.name), reverse=True)
        self.results.clear()
        self.table.blockSignals(True)
        self.table.setRowCount(len(self.items))
        for row, item in enumerate(self.items):
            checkbox = QTableWidgetItem()
            checkbox.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox.setCheckState(Qt.Unchecked)
            self.table.setItem(row, 0, checkbox)
            for col, text in enumerate([item.name, item.folder, size_text(item.size), 'On camera'], 1):
                self.table.setItem(row, col, QTableWidgetItem(text))
            self.table.setRowHeight(row, 43)
        self.table.blockSignals(False)
        self.filter_rows()
        self.status.setText(f'{len(items)} files ready to browse.' if items else 'The camera returned no files. Check the card and camera transfer state.')

    def refresh(self) -> None:
        self.status.setText('Reading the camera card…')
        self.task(self.bridge.media, self.populate)

    def disconnect(self) -> None:
        self.status.setText('Disconnecting safely…')
        def done(_: Any) -> None:
            self.camera = None
            self.populate([])
            self.status.setText('Camera disconnected.')
        self.task(self.bridge.disconnect, done)

    def choose_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, 'Import originals into…', str(self.destination))
        if folder:
            self.destination = Path(folder)
            self.folder_label.setText(folder)

    def open_folder(self) -> None:
        self.destination.mkdir(parents=True, exist_ok=True)
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.destination)))

    def filter_rows(self, *_: Any) -> None:
        text = self.search.text().casefold()
        kind = self.kind.currentText()
        for row, item in enumerate(self.items):
            self.table.setRowHidden(row, text not in f'{item.name} {item.folder}'.casefold() or (kind != 'All files' and item.kind != kind))
        self._state()

    def select_visible(self, checked: bool) -> None:
        self.table.blockSignals(True)
        for row in range(len(self.items)):
            if not self.table.isRowHidden(row):
                self.table.item(row, 0).setCheckState(Qt.Checked if checked else Qt.Unchecked)
        self.table.blockSignals(False)
        self._state()

    def stop_queue(self) -> None:
        self.stop.set()
        self.stop_button.setEnabled(False)
        self.status.setText('Finishing the current file, then stopping…')

    def import_selected(self) -> None:
        items = self.selected()
        if not items or self.camera is None:
            return
        self.stop.clear()
        service = TransferService(self.bridge, self.receipts)
        camera_uid = self.camera.uid
        destination = self.destination
        job = Job(lambda: service.run(items, camera_uid, destination, self.stop,
                                      job.signals.progress.emit, job.signals.imported.emit))
        self._job = job
        self.busy = True
        self._started = time.monotonic()
        self.stop_button.show()
        self.stop_button.setEnabled(True)
        self.status.setText(f'Importing {len(items)} files…')
        job.signals.progress.connect(self.transfer_progress)
        job.signals.imported.connect(self.imported)
        job.signals.failed.connect(self._failed)
        job.signals.done.connect(lambda results: self._finished(self.import_complete, results))
        self._state()
        self.pool.start(job)

    def transfer_progress(self, item: Media, count: int, total: int) -> None:
        self.progress.setRange(0, 1000)
        self.progress.setValue(int(min(1, count / max(1, total)) * 1000))
        self.progress_label.setText(f'{item.name} · {size_text(count)} / {size_text(total)}')

    def imported(self, result: ImportResult) -> None:
        for row, item in enumerate(self.items):
            if item.handle == result.handle:
                self.results[item.handle] = result
                self.table.item(row, 4).setText(result.status)
                self.table.item(row, 4).setForeground(QColor('#c3e0b4'))
                self.table.item(row, 0).setCheckState(Qt.Unchecked)
                break

    def import_complete(self, results: list[ImportResult]) -> None:
        imported = sum(r.status == 'Imported' for r in results)
        skipped = len(results) - imported
        self.status.setText(f'{"Queue stopped" if self.stop.is_set() else "Import complete"} · {imported} imported · {skipped} already saved')
        self.progress_label.setText('Double-click an imported file to preview it. Use Finder’s Share menu to send it on.')
        self.progress.setValue(1000 if not self.stop.is_set() else self.progress.value())

    def quick_look(self, row: int, _: int) -> None:
        result = self.results.get(self.items[row].handle)
        if result:
            if sys.platform == 'darwin':
                subprocess.Popen(['/usr/bin/qlmanage', '-p', result.path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                QDesktopServices.openUrl(QUrl.fromLocalFile(result.path))

    def help(self) -> None:
        QMessageBox.information(self, 'Connect your Sony α6700',
            '1. Close Creators’ App / Imaging Edge connections to the camera.\n\n'
            '2. On camera: Network → Cnct./PC Remote → PC Remote Function → PC Remote: On.\n\n'
            '3. For a direct link, open Wi-Fi Direct Info. Join that SSID using the Mac’s Wi-Fi menu. '
            'Or connect camera and Mac to the same Wi-Fi access point.\n\n'
            '4. Click Find camera → Connect. Confirm pairing on camera. If authentication is enabled, '
            'use the camera’s Access Authen. Info and compare its fingerprint.\n\n'
            '5. Choose a local APFS/HFS+ folder, select files, and Import selected.\n\n'
            'Allow local network access when macOS asks. Menu labels vary with firmware. '
            'See docs/SETUP.md for troubleshooting. This is an independent app.')

    def closeEvent(self, event: Any) -> None:
        if self.busy:
            self.stop.set()
            QMessageBox.information(self, 'Finish the current operation', 'The current camera operation is still running. The queue will stop after this file. Close the window once it finishes.')
            event.ignore()
            return
        self.bridge.disconnect()
        event.accept()


def main() -> None:
    parser = argparse.ArgumentParser(description='AlphaLink wireless camera import')
    parser.add_argument('--demo', action='store_true', help='Explicit simulation; no camera access')
    args = parser.parse_args()
    support = Path.home() / 'Library' / 'Application Support' / 'AlphaLink'
    support.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=support / 'alphalink.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    app = QApplication(sys.argv[:1])
    app.setApplicationName('AlphaLink')
    app.setOrganizationName('AlphaLink')
    window = Window(demo=args.demo)
    window.show()
    sys.exit(app.exec())
