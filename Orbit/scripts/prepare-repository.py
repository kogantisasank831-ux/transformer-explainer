"""Prepare an additive Orbit/ folder and dedicated root workflow for an existing repo.

Does not push, publish, create a repository, or modify the source package.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from zipfile import ZipFile


def prepare(root: Path, destination: Path, folder: str = "Orbit") -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", folder):
        raise ValueError("Use a simple folder name containing letters, numbers, hyphens or underscores")
    destination = destination.resolve()
    target = destination / folder
    workflow = destination / ".github" / "workflows" / "orbit-desktop.yml"
    if target.exists() or workflow.exists():
        raise ValueError("The Orbit folder or dedicated workflow already exists; inspect it before replacing anything")
    template = (root / "docs" / "github-folder" / "orbit-desktop.yml").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="orbit-source-") as directory:
        archive = Path(directory) / "source.zip"
        subprocess.run([sys.executable, str(root / "scripts" / "package-source.py"), str(archive)], check=True)
        with ZipFile(archive) as source:
            files = [(entry, Path(entry.filename).parts[1:]) for entry in source.infolist() if not entry.is_dir()]
            for entry, parts in files:
                if not parts or any(part in {".", ".."} for part in parts):
                    raise ValueError("Unexpected source archive path")
                output = target.joinpath(*parts)
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(source.read(entry))
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(template.replace("__ORBIT_FOLDER__", folder), encoding="utf-8")
    return workflow


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--folder", default="Orbit")
    args = parser.parse_args()
    try:
        workflow = prepare(Path(__file__).resolve().parents[1], args.destination, args.folder)
        print(f"Prepared {workflow}; no GitHub changes were made.")
    except (ValueError, OSError) as error:
        raise SystemExit(str(error)) from error

