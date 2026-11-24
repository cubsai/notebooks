# Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cubsai/notebooks/main?urlpath=lab)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cubsai/notebooks/blob/colab/index.ipynb)

Practice notebooks for an AI degree: a space to run, change and experiment
with lesson notebooks and try out ideas.

Course materials, lesson summaries and task tracking live in a separate,
private course repo, which keeps the original notebooks with their outputs for
reference. This repo is where you work on your own copies. Assessed work
doesn't go here: each assignment gets its own repository.

## Quick start

```sh
brew install uv just   # once per computer
just setup             # once per clone: environment, git hooks, notebooks
just check             # confirms everything works
```

Then open a notebook (`.ipynb`) in VS Code and pick the `.venv` kernel.

Nothing to install: the **Binder** badge opens everything in JupyterLab in
your browser, and the **Colab** badge opens an index of the notebooks in Google
Colab. Full instructions: [SETUP.md](SETUP.md).

Quick reference for magic commands, shortcuts, the `just` commands, the lab
libraries and common fixes: [cheatsheet.md](cheatsheet.md).

## Layout

```
notebooks/
├── ml/                 # Machine Learning
│   └── week-02/        # one folder per lesson
│       └── outputs/    # saved copies of run notebooks (`just snapshot`)
├── playground/         # small experiments with tools, not tied to a lesson
│   └── mlflow/         # tracking training runs with MLflow
├── .github/            # workflow that builds the Colab notebooks
├── pyproject.toml      # libraries (uv) and Jupytext settings
├── uv.lock             # exact versions
├── requirements.txt    # generated from uv.lock, for pip users and Binder
├── runtime.txt         # Python version for Binder
├── postBuild           # Binder step that creates the .ipynb files
├── .justfile           # `just` commands
├── SETUP.md            # how to run everything
└── cheatsheet.md       # quick reference
```

Module folders use short names (`ml`, later `ann` and others), with lesson
folders named `week-<nn>` or `session-<nn>`.

Each notebook is stored as a `.py` script in Jupytext's percent format. The
`.ipynb` is generated locally with `just notebooks` and isn't committed, except
for saved copies in `outputs/` folders. See
[How notebooks are stored](SETUP.md#how-notebooks-are-stored).
