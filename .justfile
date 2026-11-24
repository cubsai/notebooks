# List the available commands
default:
    @just --list

# First-time setup: environment, git hooks and notebooks
setup: sync hooks notebooks

# Install or update the environment from uv.lock
sync:
    uv sync

# Turn on the pre-commit hooks for this clone
hooks:
    uvx pre-commit install

# Add libraries and update requirements.txt, e.g. `just add seaborn`
add +packages: && export
    uv add {{packages}}

# Remove libraries and update requirements.txt
remove +packages: && export
    uv remove {{packages}}

# Write requirements.txt from uv.lock, for running without uv
export:
    uv export --frozen --no-dev --no-hashes --output-file=requirements.txt --quiet

# Create or update the .ipynb for every .py script (and the .py for any new notebook)
notebooks:
    uv run jupytext --sync $(find . \( -path './.*' -o -name outputs -o -name .ipynb_checkpoints \) -prune -o -path './*/*' \( -name '*.ipynb' -o -name '*.py' \) -print)

# Save a run notebook, outputs included, to its lesson's outputs/ folder, e.g. `just snapshot ml/week-02/6001CMD_Week2_Q4`
snapshot +notebooks:
    #!/usr/bin/env bash
    set -euo pipefail
    for nb in {{notebooks}}; do
      src="${nb%.py}"; src="${src%.ipynb}.ipynb"
      [ -f "$src" ] || { echo "No notebook at $src (run just notebooks first)"; exit 1; }
      dest="$(dirname "$src")/outputs/$(basename "$src")"
      mkdir -p "$(dirname "$dest")"
      cp "$src" "$dest"
      uv run jupytext --set-formats ipynb "$dest" > /dev/null
      echo "Saved $dest"
    done

# Check that this computer is set up: tools, environment, hooks and notebooks
check:
    #!/usr/bin/env bash
    failed=0
    pass() { echo "  ✓ $1"; }
    fail() { echo "  ✗ $1"; failed=1; }
    echo "Checking setup..."
    command -v uv > /dev/null && pass "uv $(uv --version | cut -d' ' -f2)" || fail "uv isn't installed: brew install uv"
    pass "just $(just --version | cut -d' ' -f2)"
    if [ -x .venv/bin/python ]; then
      v=$(.venv/bin/python -c 'import sys; print(f"{sys.version_info[0]}.{sys.version_info[1]}")')
      .venv/bin/python -c 'import sys; sys.exit(sys.version_info < (3, 12))' && pass "Python $v in .venv" || fail "Python $v in .venv is older than 3.12: rm -r .venv, then just sync"
      .venv/bin/python -c 'import numpy, scipy, pandas, matplotlib, sklearn, jupytext, ipykernel' 2> /dev/null && pass "libraries import" || fail "libraries missing: just sync"
    else
      fail "no .venv: just sync"
    fi
    [ -f "$(git rev-parse --git-path hooks/pre-commit)" ] && pass "pre-commit hooks on" || fail "pre-commit hooks off: just hooks"
    missing=$(find . \( -path './.*' -o -name outputs -o -name .ipynb_checkpoints \) -prune -o -path './*/*' -name '*.py' -print | while read -r f; do [ -f "${f%.py}.ipynb" ] || echo "$f"; done)
    [ -z "$missing" ] && pass "every script has its .ipynb" || fail "notebooks missing: just notebooks"
    if [ -x .venv/bin/python ]; then
      MPLBACKEND=Agg .venv/bin/python ml/week-02/6001CMD_Week2_Q4.py > /dev/null 2>&1 && pass "test notebook runs (ml/week-02 Q4)" || fail "test notebook failed: run it in VS Code to see the error"
    fi
    if [ "$failed" = 0 ]; then echo "All set."; else echo "Fix the ✗ items above, then run just check again."; exit 1; fi

# Open JupyterLab in the browser
lab:
    uv run --with jupyterlab jupyter lab
