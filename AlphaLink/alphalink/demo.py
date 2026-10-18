"""Explicit simulation for UI checks; never used as a camera fallback."""
from __future__ import annotations
import struct
import time
from collections.abc import Callable
from pathlib import Path
from .models import Camera, Media


def bitmap(r: int, g: int, b: int) -> bytes:
    pixels = bytes([b, g, r]) * 64 * 64
    return struct.pack('<2sIHHI', b'BM', 54 + len(pixels), 0, 0, 54) + struct.pack('<IiiHHIIiiII', 40, 64, 64, 1, 24, 0, len(pixels), 2835, 2835, 0, 0) + pixels


class DemoBridge:
    connected = False
    data = [bitmap(55, 112, 132), bitmap(173, 117, 76), bitmap(101, 137, 106)]

    def discover(self) -> list[Camera]:
        return [Camera(0, 'SIMULATED α6700', 'Demo camera', 'DEMO-ONLY', 'Wi-Fi simulation', '192.0.2.1', False)]

    def fingerprint(self, camera: Camera) -> str:
        return ''

    def connect(self, camera: Camera, username: str, password: str, fingerprint: str) -> None:
        self.connected = True

    def media(self) -> list[Media]:
        return [Media(i + 1, '2026-10-18', f'DEMO_{i+1:04d}.BMP', len(data), '20261018T153000') for i, data in enumerate(self.data)]

    def pull(self, media: Media, directory: Path, progress: Callable[[int], None]) -> None:
        data = self.data[media.handle - 1]
        with (directory / media.name).open('wb') as stream:
            for offset in range(0, len(data), 1024):
                stream.write(data[offset:offset+1024])
                stream.flush()
                progress(min(offset+1024, len(data)))
                time.sleep(0.025)

    def disconnect(self) -> None:
        self.connected = False
