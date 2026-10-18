from __future__ import annotations
import threading
from pathlib import Path
from unittest.mock import patch
import pytest
from alphalink.models import AlphaLinkError, Media
from alphalink.transfers import ReceiptStore, TransferService

PAYLOAD = b'photo-original-content\x00' * 20


class FakeCamera:
    def __init__(self, payload=PAYLOAD, fail=False):
        self.payload, self.fail, self.calls = payload, fail, 0

    def pull(self, media, directory, progress):
        self.calls += 1
        (directory / media.name).write_bytes(self.payload)
        progress(len(self.payload))
        if self.fail:
            raise AlphaLinkError('Simulated disconnect')


@pytest.fixture
def media():
    return Media(99, '2026-10-18', 'DSC00001.ARW', len(PAYLOAD), '20261018T153000')


@pytest.fixture
def setup(tmp_path):
    transport = FakeCamera()
    service = TransferService(transport, ReceiptStore(tmp_path / 'state/imports.sqlite3'))
    return transport, service, tmp_path / 'photos'


def run(service, items, root, stop=None, finished=lambda r: None, camera='camera-one'):
    return service.run(items, camera, root, stop or threading.Event(), lambda *a: None, finished)


def test_original_size_and_content_preserved(setup, media):
    transport, service, root = setup
    result = run(service, [media], root)[0]
    assert result.status == 'Imported'
    assert Path(result.path).read_bytes() == PAYLOAD
    assert not list(root.rglob('.alphalink-partial-*'))


def test_repeat_import_skips_verified_file_even_after_handle_change(setup, media):
    transport, service, root = setup
    run(service, [media], root)
    changed = Media(700, media.folder, media.name, media.size, media.captured)
    assert run(service, [changed], root)[0].status == 'Already imported'
    assert transport.calls == 1


def test_same_size_local_corruption_reimports_and_keeps_changed_file(setup, media):
    transport, service, root = setup
    original = Path(run(service, [media], root)[0].path)
    original.write_bytes(b'X' * len(PAYLOAD))
    new = Path(run(service, [media], root)[0].path)
    assert original != new
    assert original.read_bytes() == b'X' * len(PAYLOAD)
    assert new.read_bytes() == PAYLOAD


def test_existing_filename_never_overwritten(setup, media):
    _, service, root = setup
    folder = root / media.folder
    folder.mkdir(parents=True)
    existing = folder / media.name
    existing.write_bytes(b'keep me')
    imported = Path(run(service, [media], root)[0].path)
    assert imported.name == 'DSC00001 (1).ARW'
    assert existing.read_bytes() == b'keep me'


def test_new_destination_and_another_camera_do_not_share_receipts(setup, media, tmp_path):
    transport, service, root = setup
    run(service, [media], root)
    run(service, [media], tmp_path / 'another')
    run(service, [media], root, camera='camera-two')
    assert transport.calls == 3


def test_incomplete_download_not_committed(setup, media):
    transport, service, root = setup
    transport.payload = b'partial'
    with pytest.raises(AlphaLinkError, match='Incomplete'):
        run(service, [media], root)
    assert not (root / media.folder / media.name).exists()
    assert list(root.rglob('TRANSFER_INCOMPLETE.txt'))
    assert service.receipts.verified(media.identity('camera-one'), root.resolve()) is None


def test_disconnect_keeps_partial_and_retry_works(setup, media):
    transport, service, root = setup
    transport.fail = True
    with pytest.raises(AlphaLinkError, match='disconnect'):
        run(service, [media], root)
    transport.fail = False
    assert run(service, [media], root)[0].status == 'Imported'
    assert len(list(root.rglob('TRANSFER_INCOMPLETE.txt'))) == 1


def test_stop_after_current_file(setup, media):
    transport, service, root = setup
    stop = threading.Event()
    second = Media(100, media.folder, 'DSC00002.ARW', media.size, media.captured)
    results = run(service, [media, second], root, stop, lambda r: stop.set())
    assert len(results) == 1 and transport.calls == 1


def test_prestopped_queue_does_not_download(setup, media):
    transport, service, root = setup
    stop = threading.Event()
    stop.set()
    assert run(service, [media], root, stop) == []
    assert transport.calls == 0


def test_deleted_file_can_be_imported_again(setup, media):
    transport, service, root = setup
    Path(run(service, [media], root)[0].path).unlink()
    assert run(service, [media], root)[0].status == 'Imported'
    assert transport.calls == 2


def test_low_disk_space_fails_before_transfer(setup, media):
    transport, service, root = setup
    with patch('alphalink.transfers.shutil.disk_usage') as usage:
        usage.return_value.free = 1
        with pytest.raises(AlphaLinkError, match='disk space'):
            run(service, [media], root)
    assert transport.calls == 0


def test_symlink_date_folder_rejected(setup, media, tmp_path):
    _, service, root = setup
    root.mkdir()
    other = tmp_path / 'outside'
    other.mkdir()
    (root / media.folder).symlink_to(other, target_is_directory=True)
    with pytest.raises(AlphaLinkError, match='symbolic link'):
        run(service, [media], root)


def test_no_camera_identity_fails(setup, media):
    _, service, root = setup
    with pytest.raises(AlphaLinkError, match='identity'):
        run(service, [media], root, camera='|')


@pytest.mark.parametrize('name', ['../photo.jpg', '/photo.jpg', '..', '.', 'a\\b.jpg', 'bad\n.jpg', '', 'a\x00.jpg'])
def test_untrusted_filename_rejected(name):
    with pytest.raises(AlphaLinkError):
        Media(1, '2026-10-18', name, 12, '')


@pytest.mark.parametrize('folder', ['../outside', '20261018', '', '/2026-10-18'])
def test_untrusted_folder_rejected(folder):
    with pytest.raises(AlphaLinkError):
        Media(1, folder, 'safe.jpg', 12, '')


def test_more_than_four_gigabyte_metadata_is_not_truncated():
    item = Media(1, '2026-10-18', 'C0001.MP4', 5_000_000_001, '')
    assert item.size == 5_000_000_001 and item.kind == 'Video'
