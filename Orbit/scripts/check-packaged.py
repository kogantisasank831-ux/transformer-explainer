"""Run the integration smoke script using the compiled worker, not Python source."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
info=subprocess.check_output(['rustc','-vV'],text=True)
target=next(line.split(': ',1)[1] for line in info.splitlines() if line.startswith('host: '))
worker=root/'src-tauri'/'binaries'/f"orbit-engine-{target}{'.exe' if sys.platform=='win32' else ''}"
if not worker.is_file(): raise SystemExit('Build the worker first with scripts/build-engine.py')
environment=os.environ.copy();environment['ORBIT_ENGINE']=str(worker)
subprocess.run([sys.executable,str(root/'scripts'/'smoke.py')],cwd=root,env=environment,check=True)
