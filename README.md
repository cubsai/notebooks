# Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cubsai/notebooks/main?urlpath=lab)

Practice notebooks for the BSc (Hons) Artificial Intelligence (Coventry
University, delivered by PSB Academy): a space to run, change and experiment
with lesson notebooks and try out ideas.

The lesson notebooks were written by the module teaching staff and are
credited in each lesson folder's README.

Course materials, lesson summaries and task tracking live in the private course repo,
[`cubsai/course`](https://github.com/cubsai/course). Its week folders keep the
lecturers' original notebooks, with their outputs, for reference. This repo is
where you work on your own copies.

Assessed work (assignments and coursework) doesn't go here: each assignment
gets its own repository in `cubsai/`, with its own AI-use rules.

## Quick start

```sh
brew install uv just   # once per computer
just setup             # once per clone: environment, git hooks, notebooks
```

Then open a notebook (`.ipynb`) in VS Code and pick the `.venv` kernel. Or
click the Binder badge to run everything in the browser with nothing
installed. Full instructions, including Colab: [SETUP.md](SETUP.md).

## Layout

```
notebooks/
├── ml/                 # CU 6001 Machine Learning
│   └── week-02/        # one folder per week, as in the course repo
├── pyproject.toml      # libraries (uv) and Jupytext settings
├── uv.lock             # exact versions
├── requirements.txt    # generated from uv.lock, for pip users
├── .justfile           # `just` commands
├── runtime.txt         # Python version for Binder
├── postBuild           # Binder step that creates the .ipynb files
└── SETUP.md            # how to run everything
```

Module folders use the course's abbreviations (`ml`, later `ann` and others),
with lesson folders named as in the course repo (`week-02`, `session-03`).

Each notebook is stored as a `.py` script in Jupytext's percent format; the
`.ipynb` is generated locally and isn't committed. See
[How notebooks are stored](SETUP.md#how-notebooks-are-stored).
