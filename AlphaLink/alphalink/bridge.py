from __future__ import annotations

import json
import logging
import os
import queue
import subprocess
import sys
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

from .models import AlphaLinkError, Camera, Media

log = logging.getLogger(__name__)


def runtime_worker() -> Path:
    root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1]))
    return root / "runtime" / "alphalink-worker"


def encode(value: str) -> str:
    if "\x00" in value:
        raise AlphaLinkError("Embedded NUL characters are not accepted.")
    return value.encode("utf-8").hex() or "-"


class SonyBridge:
    """One persistent, serialized native SDK session. Secrets travel via stdin."""

    def __init__(self, worker: Path | None = None) -> None:
        self.worker = worker or runtime_worker()
        self._process: subprocess.Popen[str] | None = None
        self._messages: queue.Queue[str | None] = queue.Queue()
        self._lock = threading.RLock()
        self.connected = False

    def _start(self) -> None:
        if not self.worker.is_file():
            raise AlphaLinkError("Camera engine is missing. Run Setup.command with Sony's macOS SDK first.")
        self._messages = queue.Queue()
        try:
            self._process = subprocess.Popen(
                [str(self.worker)], cwd=self.worker.parent, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                text=True, encoding="utf-8", bufsize=1,
            )
        except OSError as exc:
            raise AlphaLinkError("Camera engine could not start. Rebuild it for this Mac's architecture.") from exc
        process, messages = self._process, self._messages

        def reader() -> None:
            assert process.stdout is not None
            try:
                for line in process.stdout:
                    if line.startswith("@alphalink "):
                        messages.put(line[len("@alphalink "):])
            finally:
                messages.put(None)

        threading.Thread(target=reader, daemon=True, name="sony-sdk-output").start()

    def request(self, command: str, *, timeout: float = 600,
                progress: Callable[[int], None] | None = None) -> Any:
        with self._lock:
            if self._process is None or self._process.poll() is not None:
                self.connected = False
                self._start()
            assert self._process is not None and self._process.stdin is not None
            try:
                self._process.stdin.write(command + "\n")
                self._process.stdin.flush()
                deadline = time.monotonic() + timeout
                while True:
                    line = self._messages.get(timeout=max(0.01, deadline - time.monotonic()))
                    if line is None:
                        raise AlphaLinkError("Camera engine stopped. Disconnect and reconnect the camera, then scan again.")
                    response = json.loads(line)
                    if response.get("event") == "progress":
                        if progress:
                            progress(int(response["bytes"]))
                        continue
                    if not response.get("ok"):
                        self.connected = False
                        raise AlphaLinkError(str(response.get("error", "Camera operation failed.")))
                    return response.get("data")
            except queue.Empty as exc:
                self._terminate()
                raise AlphaLinkError("Camera operation timed out; its session was closed. Reconnect before retrying.") from exc
            except (OSError, ValueError) as exc:
                self._terminate()
                raise AlphaLinkError("Camera engine communication failed. Reconnect and retry.") from exc

    def discover(self) -> list[Camera]:
        return [Camera(**item) for item in self.request("scan", timeout=30)]

    def fingerprint(self, camera: Camera) -> str:
        return str(self.request(f"fingerprint {camera.index}", timeout=30))

    def connect(self, camera: Camera, username: str, password: str, fingerprint: str) -> None:
        if not camera.wireless:
            raise AlphaLinkError("Select a camera discovered over Wi-Fi. Disconnect USB and check Wi-Fi setup.")
        self.request(f"connect {camera.index} {encode(username)} {encode(password)} {encode(fingerprint)}", timeout=75)
        self.connected = True

    def media(self) -> list[Media]:
        if not self.connected:
            raise AlphaLinkError("Connect to the camera first.")
        return [Media(**item) for item in self.request("list")]

    def pull(self, media: Media, directory: Path, progress: Callable[[int], None]) -> None:
        if not self.connected:
            raise AlphaLinkError("Camera is disconnected. Reconnect before importing.")
        # Large video files may take much longer than a few minutes on camera Wi-Fi.
        timeout = max(300, min(86400, int(media.size / 100_000) + 120))
        self.request(f"pull {media.handle} {encode(str(directory))} {encode(media.name)} {timeout}",
                     timeout=timeout + 60, progress=progress)

    def disconnect(self) -> None:
        with self._lock:
            try:
                if self._process and self._process.poll() is None:
                    self.request("quit", timeout=35)
                    self._process.wait(timeout=5)
            finally:
                self._terminate()

    def _terminate(self) -> None:
        self.connected = False
        process, self._process = self._process, None
        if process:
            if process.poll() is None:
                process.kill()
            process.wait(timeout=5)
            if process.stdin:
                process.stdin.close()
            if process.stdout:
                process.stdout.close()
