#!/usr/bin/env bash
set -e

if command -v python3.12 >/dev/null 2>&1; then
  PY=python3.12
elif [ -x /opt/homebrew/opt/python@3.12/bin/python3.12 ]; then
  PY=/opt/homebrew/opt/python@3.12/bin/python3.12
else
  echo "Python 3.12 not found."
  echo "On Mac, install it with:"
  echo "  brew install python@3.12"
  exit 1
fi

$PY -m venv v
. v/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt

ollama pull gemma3:4b
ollama pull nomic-embed-text

mkdir -p dart-rag-docs
echo "Setup complete. Run: . v/bin/activate && python r.py"
