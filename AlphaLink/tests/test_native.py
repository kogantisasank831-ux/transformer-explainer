"""Optional native integration: SONY_SDK_HEADERS=/path/to/RemoteCli/app/CRSDK pytest."""
import os
import shutil
import subprocess
from pathlib import Path
import pytest
from alphalink.bridge import SonyBridge, encode
from alphalink.models import AlphaLinkError


@pytest.fixture(scope='module')
def worker(tmp_path_factory):
    headers = os.environ.get('SONY_SDK_HEADERS')
    compiler = shutil.which('c++')
    if not headers or not compiler:
        pytest.skip('Set SONY_SDK_HEADERS and provide a C++ compiler for native simulator checks')
    project = Path(__file__).resolve().parents[1]
    output = tmp_path_factory.mktemp('native') / 'alphalink-worker'
    subprocess.run([compiler, '-std=c++17', '-w', '-pthread', '-I', headers,
                    str(project/'native/worker.cpp'), str(project/'tests/native_sdk_simulator.cpp'),
                    '-o', str(output)], check=True, capture_output=True, text=True)
    return output


def connected(worker):
    bridge = SonyBridge(worker)
    camera = bridge.discover()[0]
    fingerprint = bridge.fingerprint(camera)
    assert fingerprint == 'SHA256:SIMULATED'
    assert camera.name == 'Camera "test"'
    bridge.connect(camera, 'admin', 'unicode-फोटो', fingerprint)
    return bridge


def test_native_discovery_connect_list_async_download_and_disconnect(worker, tmp_path):
    bridge = connected(worker)
    try:
        media = bridge.media()[0]
        progress = []
        bridge.pull(media, tmp_path, progress.append)
        assert (tmp_path / media.name).read_bytes() == b'DATAEND!'
        assert progress and progress[-1] == 8
    finally:
        bridge.disconnect()


def test_native_rejects_unapproved_fingerprint(worker):
    bridge = SonyBridge(worker)
    try:
        camera = bridge.discover()[0]
        with pytest.raises(AlphaLinkError, match='fingerprint'):
            bridge.connect(camera, 'admin', 'secret', '')
    finally:
        bridge.disconnect()


def test_native_connection_callback_error_is_visible(worker, monkeypatch):
    monkeypatch.setenv('ALPHALINK_SIM_SCENARIO', 'connect-error')
    bridge = SonyBridge(worker)
    try:
        camera = bridge.discover()[0]
        with pytest.raises(AlphaLinkError, match='callback'):
            bridge.connect(camera, 'admin', 'secret', bridge.fingerprint(camera))
    finally:
        bridge.disconnect()


def test_native_transfer_callback_error_keeps_partial(worker, monkeypatch, tmp_path):
    monkeypatch.setenv('ALPHALINK_SIM_SCENARIO', 'transfer-error')
    bridge = connected(worker)
    try:
        media = bridge.media()[0]
        with pytest.raises(AlphaLinkError, match='callback'):
            bridge.pull(media, tmp_path, lambda n: None)
        assert (tmp_path / media.name).read_bytes() == b'DATA'
        assert not bridge.connected
    finally:
        bridge.disconnect()


def test_native_timeout_cancels_closes_session_and_returns_error(worker, monkeypatch, tmp_path):
    monkeypatch.setenv('ALPHALINK_SIM_SCENARIO', 'timeout')
    bridge = connected(worker)
    try:
        with pytest.raises(AlphaLinkError, match='timed out'):
            bridge.request(f'pull 7 {encode(str(tmp_path))} {encode("DSC00001.JPG")} 5', timeout=20)
        assert not bridge.connected
    finally:
        bridge.disconnect()
