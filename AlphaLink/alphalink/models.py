from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


class AlphaLinkError(Exception):
    """A failure suitable for display without exposing credentials."""


@dataclass(frozen=True)
class Camera:
    index: int
    model: str
    name: str
    uid: str
    connection: str
    ip: str
    ssh: bool

    @property
    def wireless(self) -> bool:
        # SDK calls wireless PTP/IP "IP"/"Ethernet" in some versions.
        return "USB" not in self.connection.upper() and bool(self.ip)


@dataclass(frozen=True)
class Media:
    handle: int
    folder: str
    name: str
    size: int
    captured: str

    def __post_init__(self) -> None:
        if (not self.name or self.name in {".", ".."}
                or "/" in self.name or "\\" in self.name
                or any(ord(c) < 32 for c in self.name)
                or len(self.name.encode("utf-8")) > 240):
            raise AlphaLinkError("Camera reported an unsafe filename.")
        if self.size < 0 or self.handle < 0:
            raise AlphaLinkError("Camera reported invalid file metadata.")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", self.folder):
            raise AlphaLinkError("Unexpected camera date folder. Refresh or update the camera firmware.")

    @property
    def kind(self) -> str:
        ext = Path(self.name).suffix.lower()
        if ext in {".arw", ".raw"}:
            return "RAW"
        if ext in {".mp4", ".mov", ".mts", ".mxf"}:
            return "Video"
        if ext in {".jpg", ".jpeg", ".hif", ".heif", ".heic", ".bmp"}:
            return "Photo"
        return "Other"

    def identity(self, camera_uid: str) -> str:
        # Handles are session-local. Do not use them for duplicate detection.
        payload = [camera_uid, self.folder, self.name, self.size, self.captured]
        return hashlib.sha256(json.dumps(payload, ensure_ascii=False).encode()).hexdigest()
