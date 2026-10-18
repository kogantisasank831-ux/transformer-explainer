"""Create a clean source ZIP without build caches or platform binaries."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
destination=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root.parent/'Orbit_Desktop_App.zip'
files=[]
for path in root.rglob('*'):
    if not path.is_file(): continue
    parts=path.relative_to(root).parts
    if any(part in {'target','node_modules','dist','build','.venv','__pycache__','.pytest_cache','gen','binaries'} for part in parts): continue
    if parts[0] not in {'crates','src-tauri','ui','engine','scripts','docs','.github','.gitignore','Cargo.toml','Cargo.lock','package.json','package-lock.json','index.html','README.md','LICENSE'}: continue
    files.append(path)
files.sort()
checksums=''.join(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(root).as_posix()}\n' for path in files)
destination.parent.mkdir(parents=True,exist_ok=True)
with ZipFile(destination,'w',ZIP_DEFLATED) as archive:
    for path in files: archive.write(path,'Orbit/'+path.relative_to(root).as_posix())
    archive.writestr('Orbit/CHECKSUMS.txt',checksums)
print(f'{destination}: {len(files)} source files, {destination.stat().st_size:,} bytes')
