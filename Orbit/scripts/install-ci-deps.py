"""Install worker dependencies into a clean CI environment, then expose its Python.

Cryptography's binary wheels carry their own OpenSSL. This avoids mixing a
runner's preinstalled dynamic cryptography build with Python's bundled libssl.
"""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
venv = root / ".venv"
subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
bin_dir = venv / ("Scripts" if sys.platform == "win32" else "bin")
python = bin_dir / ("python.exe" if sys.platform == "win32" else "python")
subprocess.run([str(python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run([str(python), "-m", "pip", "install", "--no-cache-dir", "--only-binary=cryptography",
                "-r", str(root / "engine" / "requirements-dev.txt")], check=True)
github_path = os.environ.get("GITHUB_PATH")
if github_path:
    with Path(github_path).open("a", encoding="utf-8") as output:
        output.write(str(bin_dir) + "\n")
print(f"Worker dependencies installed in {venv}")
