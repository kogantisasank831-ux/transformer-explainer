import os
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from alphalink.gui import Window


def test_demo_ui_selection_filters_and_large_progress(tmp_path):
    app = QApplication.instance() or QApplication([])
    window = Window(demo=True, data_dir=tmp_path / 'state')
    camera = window.bridge.discover()[0]
    window.bridge.connect(camera, '', '', '')
    window.camera = camera
    window.populate(window.bridge.media())
    window.select_visible(True)
    assert len(window.selected()) == 3
    assert window.import_button.isEnabled()
    window.search.setText('0001')
    assert len(window.selected()) == 1
    window.transfer_progress(window.items[0], 5_000_000_001, 6_000_000_000)
    assert window.progress.value() == 833
    assert '5000.0 MB' in window.progress_label.text()
    window.search.clear()
    window.select_visible(False)
    assert not window.import_button.isEnabled()
    window.close()
    app.processEvents()
