import importlib.util
from pathlib import Path
import zipfile
import pytest

script = Path(__file__).resolve().parents[1] / 'scripts/build_mac.py'
spec = importlib.util.spec_from_file_location('build_mac', script)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def test_archive_path_traversal_is_rejected(tmp_path):
    archive = tmp_path / 'bad.zip'
    with zipfile.ZipFile(archive, 'w') as z:
        z.writestr('../outside.txt', 'bad')
    with pytest.raises(ValueError, match='unsafe path'):
        build.extract(archive, tmp_path / 'out')
    assert not (tmp_path / 'outside.txt').exists()


def test_archive_symlinks_are_rejected(tmp_path):
    archive = tmp_path / 'bad.zip'
    entry = zipfile.ZipInfo('link')
    entry.create_system = 3
    entry.external_attr = 0o120777 << 16
    with zipfile.ZipFile(archive, 'w') as z:
        z.writestr(entry, '/outside')
    with pytest.raises(ValueError, match='symbolic link'):
        build.extract(archive, tmp_path / 'out')


def test_extracted_sdk_layout_resolves(tmp_path):
    remote = tmp_path / 'RemoteCli'
    headers = remote / 'app/CRSDK'
    libs = remote / 'external/crsdk'
    headers.mkdir(parents=True)
    libs.mkdir(parents=True)
    (headers / 'CameraRemote_SDK.h').touch()
    (libs / 'libCr_Core.dylib').touch()
    assert build.sdk_root(tmp_path, tmp_path / 'temp') == remote


def test_missing_sdk_has_actionable_error(tmp_path):
    with pytest.raises(RuntimeError, match='macOS Sony'):
        build.sdk_root(tmp_path, tmp_path / 'temp')
