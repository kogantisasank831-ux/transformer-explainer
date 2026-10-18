import sys
import textwrap
from pathlib import Path
import pytest
from alphalink.bridge import SonyBridge, encode
from alphalink.models import AlphaLinkError


@pytest.fixture
def bridge(tmp_path):
    worker = tmp_path / 'worker'
    worker.write_text(f'#!{sys.executable}\n' + textwrap.dedent('''
        import json, sys, time
        for line in sys.stdin:
            cmd = line.strip()
            if cmd == 'hang':
                time.sleep(5)
            elif cmd == 'crash':
                sys.exit(4)
            elif cmd == 'error':
                print('@alphalink ' + json.dumps({'ok': False, 'error': 'camera busy'}), flush=True)
            else:
                print('SDK non-protocol diagnostic', flush=True)
                if cmd == 'progress':
                    print('@alphalink ' + json.dumps({'event': 'progress', 'bytes': 5000000001}), flush=True)
                print('@alphalink ' + json.dumps({'ok': True, 'data': []}), flush=True)
                if cmd == 'quit':
                    break
    '''))
    worker.chmod(0o755)
    client = SonyBridge(worker)
    yield client
    client.disconnect()


def test_framed_protocol_ignores_sdk_output_and_keeps_large_progress(bridge):
    seen = []
    assert bridge.request('progress', progress=seen.append) == []
    assert seen == [5_000_000_001]
    assert bridge.discover() == []


def test_sdk_error_is_visible(bridge):
    with pytest.raises(AlphaLinkError, match='camera busy'):
        bridge.request('error')


def test_hung_worker_is_killed(bridge):
    with pytest.raises(AlphaLinkError, match='timed out'):
        bridge.request('hang', timeout=0.05)
    assert bridge._process is None


def test_worker_crash_is_visible(bridge):
    with pytest.raises(AlphaLinkError, match='stopped'):
        bridge.request('crash')


def test_missing_engine_has_setup_hint(tmp_path):
    with pytest.raises(AlphaLinkError, match='Setup.command'):
        SonyBridge(tmp_path / 'missing').discover()


def test_unicode_passwords_and_paths_do_not_become_shell_commands():
    text = 'space / फोटो $() ` ;\t\n'
    assert bytes.fromhex(encode(text)).decode() == text
    assert encode('') == '-'
    with pytest.raises(AlphaLinkError):
        encode('bad\x00')
