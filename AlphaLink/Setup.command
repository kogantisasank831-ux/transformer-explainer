#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "Run this setup on your Mac."
  exit 1
fi
if ! xcode-select -p >/dev/null 2>&1; then
  echo "Install Apple's Command Line Tools first: xcode-select --install"
  exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "Install Python 3.11–3.13 from python.org, then run setup again."
  exit 1
fi
python3 -c 'import sys; assert (3,11) <= sys.version_info[:2] < (3,14), "Use Python 3.11, 3.12 or 3.13 from python.org"'
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e '.[build,test]'
.venv/bin/python -m pytest -q
if [[ $# -gt 0 ]]; then
  .venv/bin/python scripts/build_mac.py --sdk "$1"
else
  .venv/bin/python scripts/build_mac.py --choose-sdk
fi
open -R dist/AlphaLink.app
printf '\nAlphaLink is ready in the dist folder. Press Return to close.\n'
read -r _
