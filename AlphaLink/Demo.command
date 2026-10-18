#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
if [[ ! -x .venv/bin/python ]]; then
  echo "Run Setup.command first, or create a Python environment and pip install -e ."
  exit 1
fi
exec .venv/bin/python -m alphalink --demo
