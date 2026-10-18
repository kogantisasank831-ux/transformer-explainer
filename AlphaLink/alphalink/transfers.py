from __future__ import annotations

import hashlib
import json
import logging
import os
import shutil
import sqlite3
import tempfile
import threading
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .models import AlphaLinkError, Media

log = logging.getLogger(__name__)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(4 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


class Transport(Protocol):
    def pull(self, media: Media, directory: Path, progress: Callable[[int], None]) -> None: ...


class ReceiptStore:
    """SQLite receipts. Every skip rechecks both size and a local SHA-256."""

    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        with sqlite3.connect(path) as db:
            db.execute("CREATE TABLE IF NOT EXISTS imports (identity TEXT, root TEXT, path TEXT, size INTEGER, sha256 TEXT, PRIMARY KEY(identity, root))")

    def verified(self, identity: str, root: Path) -> Path | None:
        with sqlite3.connect(self.path) as db:
            row = db.execute("SELECT path, size, sha256 FROM imports WHERE identity=? AND root=?", (identity, str(root))).fetchone()
        if not row:
            return None
        path = Path(row[0])
        try:
            if root not in path.resolve().parents or path.is_symlink():
                return None
            if path.stat().st_size == row[1] and sha256_file(path) == row[2]:
                return path
        except OSError:
            return None
        return None

    def save(self, identity: str, root: Path, path: Path, size: int, digest: str) -> None:
        with sqlite3.connect(self.path) as db:
            db.execute("INSERT OR REPLACE INTO imports VALUES (?, ?, ?, ?, ?)", (identity, str(root), str(path), size, digest))


@dataclass(frozen=True)
class ImportResult:
    name: str
    status: str
    path: str
    handle: int = 0


class TransferService:
    def __init__(self, transport: Transport, receipts: ReceiptStore) -> None:
        self.transport = transport
        self.receipts = receipts

    def run(self, media: Iterable[Media], camera_uid: str, destination: Path,
            stop: threading.Event, progress: Callable[[Media, int, int], None],
            finished: Callable[[ImportResult], None]) -> list[ImportResult]:
        root = destination.expanduser().resolve()
        root.mkdir(parents=True, exist_ok=True)
        results: list[ImportResult] = []
        if not camera_uid.strip("|"):
            raise AlphaLinkError("Camera identity unavailable; reconnect before importing.")
        for item in media:
            if stop.is_set():
                break
            identity = item.identity(camera_uid)
            verified = self.receipts.verified(identity, root)
            if verified:
                result = ImportResult(item.name, "Already imported", str(verified), item.handle)
            else:
                result = self._import(item, identity, root, progress)
            results.append(result)
            finished(result)
        return results

    def _import(self, item: Media, identity: str, root: Path,
                progress: Callable[[Media, int, int], None]) -> ImportResult:
        folder = root / item.folder
        if folder.is_symlink():
            raise AlphaLinkError("The import date folder must not be a symbolic link.")
        folder.mkdir(exist_ok=True)
        if shutil.disk_usage(root).free < item.size + 64 * 1024 * 1024:
            raise AlphaLinkError(f"Not enough free disk space to import {item.name}.")
        staging = Path(tempfile.mkdtemp(prefix=".alphalink-partial-", dir=folder))
        candidate = staging / item.name
        committed = False
        try:
            progress(item, 0, item.size)
            self.transport.pull(item, staging, lambda n: progress(item, n, item.size))
            if not candidate.is_file() or candidate.is_symlink() or candidate.stat().st_size != item.size:
                raise AlphaLinkError(f"Incomplete transfer of {item.name}. It was not added to your imports.")
            # A local checksum detects later local changes; it is not a camera-side checksum.
            digest = sha256_file(candidate)
            with candidate.open("rb") as stream:
                os.fsync(stream.fileno())
            target = folder / item.name
            for counter in range(1, 100_001):
                try:
                    # Same-filesystem hard link is atomic and never overwrites an existing file.
                    os.link(candidate, target)
                    break
                except FileExistsError:
                    target = folder / f"{Path(item.name).stem} ({counter}){Path(item.name).suffix}"
                except OSError as exc:
                    raise AlphaLinkError("Import folder must support atomic hard links (use APFS or HFS+ on this Mac).") from exc
            else:
                raise AlphaLinkError("Too many files with the same name in the import folder.")
            self.receipts.save(identity, root, target, item.size, digest)
            committed = True
            progress(item, item.size, item.size)
            log.info("Imported %s (%s bytes)", item.name, item.size)
            return ImportResult(item.name, "Imported", str(target), item.handle)
        except Exception:
            # Retain partial data for inspection/recovery; no partial is presented as complete.
            try:
                (staging / "TRANSFER_INCOMPLETE.txt").write_text(
                    "This folder is an unfinished AlphaLink transfer. Reconnect and import again.\n"
                    "No byte-range resume is supported. You may delete this folder when the app is closed.\n", encoding="utf-8")
            except OSError:
                pass
            raise
        finally:
            # Only clean after receipt commit. Failures retain their staging directory.
            if committed:
                shutil.rmtree(staging, ignore_errors=True)
