# Cheat sheet

Quick reference for working in this repo: Jupyter magic commands, the
notebook script format, keyboard shortcuts, the `just` and `uv` commands, the
libraries used in the labs, and fixes for common problems.

- [Magic commands](#magic-commands)
- [Shell commands](#shell-commands)
- [Getting help](#getting-help)
- [Notebook scripts (`py:percent`)](#notebook-scripts-pypercent)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [Commands in this repo](#commands-in-this-repo)
- [Library quick reference](#library-quick-reference)
- [Troubleshooting](#troubleshooting)

## Magic commands

Magic commands are instructions to Jupyter (IPython), not Python. They only
work inside a notebook (or IPython), never in a plain `python` script.

- **Line magics** start with `%` and apply to that one line.
- **Cell magics** start with `%%`, must be the first line of the cell, and
  apply to the whole cell.
- `%lsmagic` lists every magic available; `%magic` explains them.

### Plotting

| Command | What it does |
| ------- | ------------ |
| `%matplotlib inline` | Show matplotlib charts under the cell as static images (the default in modern Jupyter, VS Code and Colab, but harmless to keep) |
| `%matplotlib widget` | Interactive, zoomable charts (needs the `ipympl` library) |

### Timing and profiling

| Command | What it does |
| ------- | ------------ |
| `%time expr` | Run a line once and report how long it took |
| `%%time` | Time the whole cell, once |
| `%timeit expr` | Run a line many times and report the average, for comparing approaches |
| `%%timeit` | The same for a whole cell |
| `%prun expr` | Profile a line: which functions took the time |

```python
%timeit sum(range(1_000))
%timeit np.arange(1_000).sum()   # compare with NumPy
```

### Variables and the session

| Command | What it does |
| ------- | ------------ |
| `%who` | List the variables you've defined |
| `%whos` | The same, with each variable's type and value |
| `%reset -f` | Delete all your variables (a clean slate without restarting the kernel) |
| `%history -n` | Show the code you've run, with line numbers |

### Files and folders

| Command | What it does |
| ------- | ------------ |
| `%pwd` | Show the current folder |
| `%cd path` | Change folder (stays changed for later cells, unlike `!cd`) |
| `%ls` | List files in the current folder |
| `%run script.py` | Run a Python file and bring its variables into the notebook |
| `%load script.py` | Paste a file's contents into the cell |
| `%%writefile name.py` | Save the rest of the cell as a file instead of running it |

### Installing and environment

| Command | What it does |
| ------- | ------------ |
| `%pip install seaborn` | Install a library into the environment the notebook is running in |
| `%env` | Show environment variables; `%env NAME=value` sets one |

Use `%pip`, not `!pip`: `!pip` can install into a different Python from the
one the notebook uses. In this repo, prefer `just add seaborn` in a terminal,
so the library is recorded in `pyproject.toml` and everyone (Binder, Colab,
other computers) gets it. `%pip` is fine for a quick try or in Colab.

### Debugging and reloading

| Command | What it does |
| ------- | ------------ |
| `%debug` | After an error, open the debugger at the point it failed (`q` to quit) |
| `%load_ext autoreload` then `%autoreload 2` | Re-import your own `.py` modules automatically when you change them |
| `%%capture output` | Run the cell without printing; the output is saved in `output` |

## Shell commands

A line starting with `!` runs a terminal command from the notebook:

```python
!ls -la
!head -5 data.csv          # peek at a CSV file
files = !ls *.csv          # capture the output as a list
```

Each `!` line runs in its own shell, so `!cd folder` doesn't stick: use
`%cd folder` instead.

## Getting help

| Type | What you get |
| ---- | ------------ |
| `len?` | The help text for a function or object |
| `pd.read_csv?` | The full parameter list |
| `pd.read_csv??` | The source code, where available |
| `pd.read_*?` | Everything matching a pattern |
| `help(pd.read_csv)` | Plain Python help (works anywhere) |

In VS Code you can also hover over a name, or press ⌘ and click to jump to its
definition.

## Notebook scripts (`py:percent`)

Notebooks are stored in this repo as `.py` scripts in Jupytext's percent
format. How each kind of content is written:

| In the notebook | In the `.py` script |
| --------------- | ------------------- |
| A new code cell | `# %%` on its own line |
| A code cell with a title | `# %% Load the data` |
| A markdown cell | `# %% [markdown]`, then each line as a comment: `# ## A heading` |
| `%matplotlib inline` | `# %matplotlib inline` |
| `%%time` | `# %%time` (first line of the cell) |
| `!pip install seaborn` | `# !pip install seaborn` |

```python
# %% [markdown]
# # Linear regression
# Predict restaurant profit from city population.

# %%
# %matplotlib inline
import pandas as pd

# %% Load the data
df = pd.read_csv("Rest_Pop_Profit.csv")
df.head()
```

Rules that keep pairing working:

- Every cell starts with a line that is exactly `# %%` (optionally followed by
  a title or `[markdown]`).
- Magics and shell commands are always commented out in the script. An
  uncommented one makes Jupytext read the file as a different format, and it
  reports "is not a paired notebook".
- Use Unix (LF) line endings.

Full steps: [Converting a script into a notebook](SETUP.md#converting-a-script-into-a-notebook).

## Keyboard shortcuts

Notebooks have two modes: **edit mode** (typing in a cell) and **command
mode** (acting on cells). Press **Esc** for command mode, **Enter** to edit.

| Action | Jupyter and VS Code | Colab |
| ------ | ------------------- | ----- |
| Run cell, move to next | Shift+Enter | Shift+Enter |
| Run cell, stay | Ctrl+Enter | Ctrl/⌘+Enter |
| Run cell, insert below | Alt/Option+Enter | Alt/Option+Enter |
| Insert cell above / below | A / B (command mode) | Ctrl/⌘+M, then A / B |
| Delete cell | D, D (command mode) | Ctrl/⌘+M, then D |
| Change to markdown / code | M / Y (command mode) | Ctrl/⌘+M, then M / Y |
| Undo cell deletion | Z (command mode) | Ctrl/⌘+M, then Z |
| Comment / uncomment lines | ⌘+/ | Ctrl/⌘+/ |
| Show all shortcuts | ⌘+Shift+P, then "keyboard shortcuts" (VS Code) | Ctrl/⌘+M, then H |

## Commands in this repo

### `just`

| Command | What it does |
| ------- | ------------ |
| `just` | List the commands |
| `just setup` | First-time setup: environment, git hooks, notebooks |
| `just check` | Check this computer is set up |
| `just sync` | Install or update the environment from `uv.lock` |
| `just notebooks` | Create or update the `.ipynb` for every `.py` script |
| `just snapshot <notebook>` | Save a run notebook with its outputs to `outputs/` |
| `just add <library>` | Add a library (updates `requirements.txt` too) |
| `just remove <library>` | Remove a library |
| `just export` | Regenerate `requirements.txt` |
| `just lab` | Open JupyterLab in the browser |

### `uv`

| Command | What it does |
| ------- | ------------ |
| `uv run python script.py` | Run a script with the project's environment, no activating needed |
| `uv run jupytext --sync file.py` | Pair one notebook |
| `uv tree` | Show the installed libraries and what depends on what |
| `uv lock --upgrade` | Upgrade every library to its newest allowed version (then `just sync`, `just export`) |
| `uv python list` | Show the Python versions uv can use |

### Day to day

```sh
git pull                 # get the latest scripts
just sync                # if uv.lock changed
just notebooks           # rebuild your .ipynb files
# … work in VS Code …
just notebooks           # make sure each .py matches its notebook
git add -A && git commit -m "Try a polynomial fit in Week 2 Q1"
```

## Library quick reference

The calls the labs use most.

### pandas

```python
import pandas as pd

df = pd.read_csv("data.csv")       # load a CSV
df.head()                          # first 5 rows
df.shape                           # (rows, columns)
df.info()                          # column types and non-null counts
df.describe()                      # summary statistics
df.isnull().sum()                  # missing values per column
df.duplicated().sum()              # number of duplicate rows
df.nunique()                       # distinct values per column
df["col"].value_counts()           # counts of each value
df[df["Age"] > 30]                 # filter rows
X = df.iloc[:, :-1]                # all columns but the last (features)
y = df.iloc[:, -1]                 # the last column (target)
```

### NumPy

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape                            # (2, 3)
a.reshape(3, 2)                    # same data, new shape
np.arange(0, 10, 2)                # 0, 2, 4, 6, 8
np.linspace(-10, 10, 100)          # 100 evenly spaced values
np.mean(a), np.std(a), np.sqrt(a)
a ** 3                             # power: ** (not ^, which is XOR)
```

### scikit-learn

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)       # model.score() gives the same R² for regressors
```

Every model follows the same pattern: create it, `fit(X_train, y_train)`,
then `predict(X)` and `score(X, y)`. `score` is accuracy for classifiers and R²
for regressors.

### matplotlib

```python
import matplotlib.pyplot as plt

plt.scatter(x, y)                  # points
plt.plot(x, y, label="fit")        # line
plt.title("Profit vs population")
plt.xlabel("Population"); plt.ylabel("Profit")
plt.legend(); plt.grid(True)
plt.show()
```

## Troubleshooting

| Problem | Fix |
| ------- | --- |
| Jupytext: "… is not a paired notebook" | The script isn't valid `py:percent`: check each cell starts with `# %%` and magics are commented out ([rules](#notebook-scripts-pypercent)) |
| `just notebooks` skips a file | It only looks in module folders (`ml/…`), not the repo root or `outputs/` |
| VS Code asks for a kernel, or uses the wrong one | **Select Kernel → Python Environments → .venv** |
| `ModuleNotFoundError: No module named …` | `just sync`; if the library is new, `just add <library>` |
| `NameError: name 'display' is not defined` | You ran the notebook as a plain script. `display` only exists in Jupyter: run it as a notebook, or add `from IPython.display import display` |
| `FileNotFoundError` reading a CSV | The dataset must be in the same folder as the notebook; in Colab, run the first (setup) cell |
| Charts don't appear | Make sure the cell ends with `plt.show()`, or add `%matplotlib inline` in an early cell |
| Commit stops with "files were modified by this hook" | A pre-commit hook updated a file: `git add` it and commit again |
| Something else | `just check` lists what's wrong and how to fix it |
