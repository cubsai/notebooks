# Setup: running the notebooks

How to run the notebooks in this repository, on your computer or in the
cloud. Anaconda, which the lab sheets suggest, isn't needed.

- [Setup checklist](#setup-checklist)
- [How notebooks are stored](#how-notebooks-are-stored)
- [Locally: uv, just and VS Code](#locally-uv-just-and-vs-code)
- [Saving outputs](#saving-outputs)
- [Keeping `requirements.txt` in step](#keeping-requirementstxt-in-step)
- [In the cloud: Binder and Google Colab](#in-the-cloud-binder-and-google-colab)

## Setup checklist

Work through this once per computer. When every box is ticked, the computer is
ready for the labs. The steps are explained in the sections below.

**Tools (once per computer)**

- [ ] `uv --version` and `just --version` both print a version
      (if not: `brew install uv just`)
- [ ] VS Code has the **Python**, **Jupyter** and **Jupytext-Sync**
      extensions installed (Extensions view, ⇧⌘X)

**This repo (once per clone)**

- [ ] The repo is cloned (`git clone https://github.com/cubsai/notebooks.git`)
      and up to date (`git pull` on `main`)
- [ ] `just setup` finished without errors
- [ ] `just check` ends with **All set.** It checks Python 3.12+ in `.venv`,
      that the libraries import, that the git hooks are on, that every script
      has its `.ipynb`, and that a test notebook runs

**In VS Code**

- [ ] Open `ml/week-02/6001CMD_Week2_Q4.ipynb`, choose **Select Kernel →
      .venv**, then **Run All**: the weather charts appear with no errors

**Cloud fallbacks (optional)**

- [ ] The **Binder** badge in the [README](README.md) opens JupyterLab (the
      first launch after a change can take a few minutes)
- [ ] The **Colab** badge opens the notebook index, and Week 2 Q4 runs after
      its first (setup) cell

If anything fails, run `just check` again: each ✗ line says which command
fixes it.

## How notebooks are stored

Every notebook is a pair of files, kept in sync by
[Jupytext](https://jupytext.org/):

| File | What it is | In git? |
| ---- | ---------- | ------- |
| `Q1.py` | The notebook as a plain-text Python script, in the "percent" format: each `# %%` line starts a cell, and markdown cells are comment blocks | Yes: this is the source of truth |
| `Q1.ipynb` | The notebook you open and run, with its outputs | No: generated locally, ignored by git |

Why: the `.py` files have no outputs or embedded images, so diffs are small
and readable, and you can edit them in any editor. Outputs stay on your
machine. The original notebooks, with their outputs, are kept for reference
in a separate private course repo. To keep a run notebook's outputs in git,
see [Saving outputs](#saving-outputs).

Pairing is set in `pyproject.toml` under `[tool.jupytext]`, so every notebook
in the repo is paired automatically.

## Locally: uv, just and VS Code

[uv](https://docs.astral.sh/uv/) manages Python, the libraries and the virtual
environment. [just](https://just.systems/) wraps the commands you use often.
VS Code runs the notebooks.

### 1. Install the tools (once per computer)

```sh
brew install uv just
```

In VS Code, install these extensions:

- **Python** and **Jupyter** (both by Microsoft), to run notebooks
- **Jupytext-Sync**, to update the `.py` file whenever you save a notebook
  (and the other way round)

### 2. Set up the repo (once per clone)

From the repository root:

```sh
just setup
```

This runs three steps, which you can also run on their own:

| Command | What it does |
| ------- | ------------ |
| `just sync` | Creates `.venv` and installs the libraries from `uv.lock` |
| `just hooks` | Turns on the pre-commit hooks (see [below](#keeping-requirementstxt-in-step)) |
| `just notebooks` | Creates the `.ipynb` for every `.py` script, so you can open them |

You never create or activate `.venv` yourself: uv keeps it in step with
`pyproject.toml` and `uv.lock`.

### 3. Run a notebook

Open the `.ipynb` file in VS Code, choose **Select Kernel**, and pick `.venv`.

Notebooks read data files from their own folder (for example
`pd.read_csv('Rest_Pop_Profit.csv')`), so put each dataset next to the
notebook that uses it.

### 4. Day to day

| Command | What it does |
| ------- | ------------ |
| `just` | Lists the commands |
| `just check` | Checks that this computer is set up (see the [checklist](#setup-checklist)) |
| `just sync` | Updates the environment, e.g. after pulling changes to `uv.lock` |
| `just add <library>` | Adds a library to `pyproject.toml` and `uv.lock`, and updates `requirements.txt` |
| `just remove <library>` | Removes a library and updates all three files |
| `just export` | Regenerates `requirements.txt` from `uv.lock` |
| `just notebooks` | Creates or updates the `.ipynb` for every `.py` script (and the `.py` for any new notebook): whichever file is missing is created, and the older one is updated |
| `just snapshot <notebook>` | Saves a run notebook, outputs included, to its lesson's `outputs/` folder so you can commit it (see [Saving outputs](#saving-outputs)) |
| `just lab` | Opens JupyterLab in the browser, if you'd rather not use VS Code |

**Starting a new notebook:** create the `.ipynb` in VS Code, then run
`just notebooks` (or save it with Jupytext-Sync on) to create its `.py`. Only
the `.py` is committed.

**After pulling:** run `just notebooks` to bring your `.ipynb` files up to
date with the latest scripts.

### What the project files are

| File | What it is | Commit it? |
| ---- | ---------- | ---------- |
| `pyproject.toml` | The libraries the notebooks need (the standard Python format; replaces `requirements.txt`), plus the Jupytext settings | Yes |
| `uv.lock` | The exact versions installed | Yes |
| `requirements.txt` | The same libraries for people without uv | Yes (generated) |
| `.justfile` | The `just` commands | Yes |
| `.pre-commit-config.yaml` | The git hooks | Yes |
| `runtime.txt`, `postBuild` | Binder's Python version and build step | Yes |
| `.github/` | The workflow that builds the Colab notebooks | Yes |
| `.venv/` | The virtual environment | No (ignored) |

## Saving outputs

Outputs live only in your local `.ipynb`, which git ignores. To keep a run's
outputs, for example to look at them on another computer, save a copy:

```sh
just snapshot ml/week-02/6001CMD_Week2_Q4
```

This copies `ml/week-02/6001CMD_Week2_Q4.ipynb`, outputs and all, to
`ml/week-02/outputs/6001CMD_Week2_Q4.ipynb`, which git does track. Commit and
push it, and:

- on GitHub, the copy shows with its outputs, so you can read it on any device
- on another computer, pull and open the copy from `outputs/`

The copy is a snapshot: it isn't paired with the script, so editing it doesn't
change your notebook, and `just notebooks` leaves it alone. Run `just snapshot`
again to replace it with a newer run. Notebooks with many charts make big
files, so only snapshot runs you want to keep.

## Keeping `requirements.txt` in step

Anyone without uv can install the same libraries
with plain `pip` or Anaconda:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` only needs regenerating when the libraries change, not when
you edit a notebook. Two things keep it up to date:

1. **`just add` and `just remove`** regenerate it straight away.
2. **The `uv-export` pre-commit hook** regenerates it whenever `uv.lock` is
   part of a commit, in case you ran `uv add` without `just`. Set its `rev` in
   `.pre-commit-config.yaml` to your uv version (`uv --version`).

A second hook, **jupytext-sync**, updates each `.py` script from its notebook
before a commit, in case you edited the notebook without the Jupytext-Sync
extension.

If a hook changes a file, the commit stops. Stage the updated file
(`git add`) and commit again.

`requirements.txt` doesn't record the Python version. This repo needs Python
3.12 or later (`requires-python` in `pyproject.toml`); say so in any README
someone else will read.

## In the cloud: Binder and Google Colab

### Binder

[Binder](https://mybinder.org/) builds a temporary JupyterLab from this repo,
with nothing to install: click the badge in the [README](README.md), or open
<https://mybinder.org/v2/gh/cubsai/notebooks/main?urlpath=lab>.

- It reads `runtime.txt` (Python version) and installs `requirements.txt`,
  then `postBuild` runs Jupytext to create the `.ipynb` files.
- The first launch after a change takes a few minutes while Binder builds the
  image; later launches are faster.
- Sessions are temporary and changes aren't saved: download anything you want
  to keep.
- Datasets that aren't committed (large files) won't be there; upload them in
  JupyterLab.

### Google Colab

Colab only opens `.ipynb` files from GitHub, so a GitHub Action builds
Colab-ready copies of every notebook whenever `main` changes and publishes them
to the `colab` branch. Each copy starts with a cell that downloads this repo
(so the datasets are there) and moves into the notebook's folder.

- Click the **Colab** badge in the [README](README.md) for an index of all
  notebooks, or use the **Colab** links in each lesson's README.
- Run the first cell, then the rest of the notebook.
- Changes aren't saved back to GitHub. Use **File → Save a copy in Drive** to
  keep them.
- Colab already has the common libraries installed. Install anything missing
  in a cell with `!pip install <library>`.
- Don't edit the `colab` branch: it's rebuilt from `main` each time.

The **Open in Colab** Chrome extension, and replacing `github.com` with
`colab.research.google.com/github` in a URL, work for any `.ipynb` on GitHub,
including saved copies in `outputs/` folders. For notebooks in the private
course repo, Colab needs access to the organisation: in GitHub, go to
**Settings → Applications → Authorized OAuth Apps → Colaboratory** and grant
access to `cubsai`.
