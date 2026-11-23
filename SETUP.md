# Setup: running the notebooks

How to run the notebooks in this repository, on your computer or in the
cloud. Anaconda, which the lab sheets suggest, isn't needed.

- [How notebooks are stored](#how-notebooks-are-stored)
- [Locally: uv, just and VS Code](#locally-uv-just-and-vs-code)
- [Keeping `requirements.txt` in step](#keeping-requirementstxt-in-step)
- [In the cloud: Binder and Google Colab](#in-the-cloud-binder-and-google-colab)

## How notebooks are stored

Every notebook is a pair of files, kept in sync by
[Jupytext](https://jupytext.org/):

| File | What it is | In git? |
| ---- | ---------- | ------- |
| `Q1.py` | The notebook as a plain-text Python script, in the "percent" format: each `# %%` line starts a cell, and markdown cells are comment blocks | Yes: this is the source of truth |
| `Q1.ipynb` | The notebook you open and run, with its outputs | No: generated locally, ignored by git |

Why: the `.py` files have no outputs or embedded images, so diffs are small
and readable, and you can edit them in any editor. Outputs stay on your
machine. The lecturers' original notebooks, with their outputs, are kept for
reference in the private course repo.

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
| `just sync` | Updates the environment, e.g. after pulling changes to `uv.lock` |
| `just add <library>` | Adds a library to `pyproject.toml` and `uv.lock`, and updates `requirements.txt` |
| `just remove <library>` | Removes a library and updates all three files |
| `just export` | Regenerates `requirements.txt` from `uv.lock` |
| `just notebooks` | Pairs every notebook with its script: creates whichever file is missing and updates the older one |
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
| `.venv/` | The virtual environment | No (ignored) |

## Keeping `requirements.txt` in step

Anyone without uv (a lecturer, for example) can install the same libraries
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
3.12 or later (`requires-python` in `pyproject.toml`); say so in any README a
lecturer will read.

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

Colab opens `.ipynb` files, which this repo doesn't commit. Two ways round
that:

- **Upload the notebook:** generate it locally (`just notebooks`) and upload
  the `.ipynb` (and its dataset) to Colab.
- **Clone the repo inside Colab** and generate the notebooks there. This also
  brings the committed datasets along:

  ```python
  !git clone https://github.com/cubsai/notebooks.git
  %cd notebooks
  !pip install -q jupytext
  !jupytext --sync ml/week-02/*.py
  ```

  Then open the generated `.ipynb` from Colab's file browser.

Other Colab tips:

- Colab already has the common libraries installed. Install anything missing
  in a cell with `!pip install <library>`.
- The **Open in Colab** Chrome extension, and replacing `github.com` with
  `colab.research.google.com/github` in a URL, work for any `.ipynb` on
  GitHub. For notebooks in the private `cubsai/course` repo, Colab needs
  access to the organisation: in GitHub, go to **Settings → Applications →
  Authorized OAuth Apps → Colaboratory** and grant access to `cubsai`.
