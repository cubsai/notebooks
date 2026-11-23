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

# Open JupyterLab in the browser
lab:
    uv run --with jupyterlab jupyter lab
