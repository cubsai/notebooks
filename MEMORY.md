# MEMORY.md

Persistent context for agents working in this repository. Read it at the
start of every session. Keep entries short and dated (YYYY-MM-DD), and delete
them once they stop being true.

## Decisions

- 2026-11-23: Created this repo as the student's practice space for running
  and changing notebooks. The original notebooks, with outputs, stay in the
  private course repo as reference copies.
- 2026-11-23: The repo is public so Binder and Colab can run it. The student
  chose to include the lesson notebooks: they're given to students for
  practice and aren't under copyright.
- 2026-11-23: No mention of the university, the academy or any teaching staff
  anywhere in this repo (including attribution).
- 2026-11-23: Notebooks are committed as Jupytext percent scripts; `.ipynb`
  files are generated locally, except snapshots in `outputs/` (`just
  snapshot`) made to keep outputs across machines.
- 2026-11-23: Colab gets its notebooks from the `colab` branch, built by a
  GitHub Action on every push to `main`.
