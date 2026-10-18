"""Build the PDF worker on the SAME operating system and architecture as Orbit."""
from __future__ import annotations
import os
from pathlib import Path
import shutil
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
os.chdir(root)
info=subprocess.check_output(['rustc','-vV'],text=True)
target=next(line.split(': ',1)[1] for line in info.splitlines() if line.startswith('host: '))
command=[sys.executable,'-m','PyInstaller','--clean','--noconfirm','--onefile','--name','orbit-engine',
         '--distpath','engine/dist','--workpath','engine/build','--specpath','engine/build',
         '--collect-all','pypdfium2','--collect-all','pypdfium2_raw',
         '--collect-all','pdfplumber','engine/worker.py']
for module in ['numpy','pandas','scipy','matplotlib','IPython','jupyter','torch','tensorflow','cv2','sympy','tkinter']:
    command[3:3]=['--exclude-module',module]
subprocess.run(command,check=True)
extension='.exe' if sys.platform=='win32' else ''
destination=root/'src-tauri'/'binaries'/f'orbit-engine-{target}{extension}'
destination.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(root/'engine'/'dist'/f'orbit-engine{extension}',destination)
print(f'Worker built for {target}: {destination}')

