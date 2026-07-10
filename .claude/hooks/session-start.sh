#!/bin/bash
# SessionStart hook: install the Jupyter Book toolchain so the build
# (which is this project's test — see CLAUDE.md §2) works in Claude Code
# on the web. Idempotent and non-interactive.
set -euo pipefail

# Only needed in the remote (Claude Code on the web) environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# Create the venv once; reused if the container state is cached.
if [ ! -x venv/bin/python ]; then
  python3 -m venv venv
fi

# Install the build toolchain. pip skips already-satisfied deps, so this
# is cheap on a warm container and correct on a cold one.
venv/bin/pip install --quiet --upgrade pip
venv/bin/pip install --quiet -r requirements.txt

# Put the venv on PATH for the session so `jupyter-book` is available.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"${CLAUDE_PROJECT_DIR:-$PWD}/venv/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
