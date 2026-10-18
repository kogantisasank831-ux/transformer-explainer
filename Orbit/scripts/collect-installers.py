"""Copy native installers into release/ and calculate SHA-256 checksums."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def collect(root: Path, platform: str) -> list[Path]:
    expected = {"windows-x64": {".exe", ".msi"}, "macos-arm64": {".dmg"}, "macos-x64": {".dmg"}}[platform]
    source = root / "target" / "release" / "bundle"
    installers = sorted(p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in expected)
    if not installers:
        raise ValueError(f"No {platform} installers found in {source}")
    found = {p.suffix.lower() for p in installers}
    if found != expected:
        raise ValueError(f"Expected installer types {sorted(expected)}, got {sorted(found)}")
    version = json.loads((root / "package.json").read_text(encoding="utf-8"))["version"]
    destination = root / "release"
    destination.mkdir(exist_ok=True)
    # This folder belongs to this build; avoid bundling stale installers.
    if any(destination.iterdir()):
        raise ValueError("release/ is not empty. Move or remove the previous build before collecting a new one.")
    files = []
    for source_file in installers:
        target = destination / f"Orbit-{version}-{platform}{source_file.suffix.lower()}"
        if target.exists():
            raise ValueError(f"Multiple installers of the same type: {source_file.suffix}")
        shutil.copy2(source_file, target)
        files.append(target)
    checksums = "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in files)
    (destination / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8")
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", required=True, choices=["windows-x64", "macos-arm64", "macos-x64"])
    args = parser.parse_args()
    try:
        for output in collect(Path(__file__).resolve().parents[1], args.platform):
            print(output)
    except (ValueError, OSError) as error:
        raise SystemExit(str(error)) from error

