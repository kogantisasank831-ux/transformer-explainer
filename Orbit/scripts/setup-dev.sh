#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
for program in python3 node npm cargo; do
  command -v "$program" >/dev/null || { echo "Install $program first; see README.md."; exit 1; }
done
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r engine/requirements-dev.txt
npm ci
echo 'Setup complete. Run npm run desktop. LibreOffice and Tesseract are optional local installations.'

