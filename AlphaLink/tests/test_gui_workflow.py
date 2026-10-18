import os
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
import time
from pathlib import Path
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from alphalink.gui import Window


def test_gui_queue_imports_and_repeat_import_skips(tmp_path):
    app = QApplication.instance() or QApplication([])
    window = Window(demo=True, data_dir=tmp_path / 'state')
    window.destination = tmp_path / 'pictures'
    window.camera = window.bridge.discover()[0]
    window.bridge.connect(window.camera, '', '', '')
    window.populate(window.bridge.media())
    window.select_visible(True)
    window.import_selected()
    deadline = time.monotonic() + 10
    while window.busy and time.monotonic() < deadline:
        QTest.qWait(20)
    assert not window.busy
    assert len(list(window.destination.rglob('*.BMP'))) == 3
    assert '3 imported' in window.status.text()
    window.select_visible(True)
    window.import_selected()
    while window.busy and time.monotonic() < deadline:
        QTest.qWait(20)
    assert '3 already saved' in window.status.text()
    assert len(list(window.destination.rglob('*.BMP'))) == 3
    window.close()
    app.processEvents()
