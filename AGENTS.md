# AGENTS.md

Guidance for AI coding and writing agents working in this repository.

## About this repository

`cubsai/notebooks` holds the student's practice notebooks for the BSc (Hons)
Artificial Intelligence (Coventry University, delivered by PSB Academy). It
sits next to the course repo, `cubsai/course`, which holds the lesson
materials (including the lecturers' original notebooks), summaries, tasks and
the course-wide `AGENTS.md`. Read that file for context on modules, dates and
the student's preferences.

This is a learning space: agents can help freely here (explain, debug, extend
notebooks, suggest experiments). Assessed work never goes here; each
assignment has its own repository in `cubsai/` with stricter AI-use rules.

**This repository is public** (so Binder can run it). Never commit personal
information, credentials, assessment briefs or anything from an assessment
repo. Lesson notebooks copied from the course are included by the student's
choice; credit them to the module in the lesson README.

## Layout and naming

- Module folders use the course abbreviations in lowercase: `ml/` (CU 6001
  Machine Learning), `ann/` (CU 6009 Artificial Neural Networks). Ask before
  inventing one for another module.
- Lesson folders match the course repo: `week-<nn>/` or `session-<nn>/`.
- Each lesson folder has a short `README.md`: where the notebooks came from
  (credit the module and teaching staff), what each does, and which data
  files it needs.
- Keep the lecturers' file names for copied notebooks, so they're easy to match
  with the originals in the course repo.

## Notebooks

- Every notebook is a Jupytext pair: a `.py` script in percent format (tracked)
  and an `.ipynb` (ignored, generated locally). Settings are in
  `pyproject.toml` under `[tool.jupytext]`.
- Edit either file, then run `just notebooks` so both match before committing.
  Never commit `.ipynb` files.
- Every `.py` file inside a module folder is treated as a notebook. Put any
  shared helper code in a clearly named root folder instead.
- To copy a new week's notebooks from the course repo: copy the `.ipynb` files
  into the lesson folder, run `just notebooks` to create the `.py` scripts,
  add the lesson `README.md`, and commit the `.py` files and README only.

## Binder

`runtime.txt` sets the Python version, Binder installs `requirements.txt`, then
`postBuild` runs Jupytext to create the `.ipynb` files. Keep `jupytext` a main
(not dev) dependency so it's in `requirements.txt`.

## Environment

- uv manages the environment: change libraries only with `just add` or
  `just remove` (or `uv add`/`uv remove` followed by `just export`), so
  `pyproject.toml`, `uv.lock` and `requirements.txt` stay in step.
- Never add `requirements.txt` by hand or edit it directly; it's generated.
- Full instructions for the student: [SETUP.md](SETUP.md).

## Data

- Datasets live next to the notebooks that read them.
- Small CSVs can be committed. Don't commit large files: name them
  `*.large.csv` (git-ignored) or note in the lesson README where to get them.

## Git

Same workflow as the course repo: agents may commit and push their own
changes, through a pull request that the student reviews.

1. Branch from an up-to-date `main`, named `agent/<short-topic>`.
2. Commit with a clear message in the imperative mood.
3. Push and open a pull request against `main` with a short summary.
4. Merge only when the student explicitly approves that pull request in chat,
   using a rebase merge, then delete the branch.
5. Never push to `main` directly, force-push, or rewrite pushed history.
6. Commit only the agent's own changes.
