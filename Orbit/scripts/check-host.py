"""Fail clearly if an Actions runner uses the wrong native architecture."""
from __future__ import annotations
import os
import subprocess

expected = os.environ.get("ORBIT_EXPECTED_TARGET")
info = subprocess.check_output(["rustc", "-vV"], text=True)
actual = next(line.split(": ", 1)[1] for line in info.splitlines() if line.startswith("host: "))
if expected and actual != expected:
    raise SystemExit(f"Expected native host {expected}, got {actual}. Use the matching runner.")
print(f"Native build host: {actual}")

