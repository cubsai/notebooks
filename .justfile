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

# Pair every notebook with its .py script, creating whichever is missing
notebooks:
    uv run jupytext --sync $(find . -path ./.venv -prune -o -path '*/.ipynb_checkpoints' -prune -o \( -name '*.ipynb' -o -name '*.py' \) -print)

# Open JupyterLab in the browser
lab:
    uv run --with jupyterlab jupyter lab
