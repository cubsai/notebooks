# MLflow basics

A small, self-contained example of how [MLflow](https://mlflow.org/) tracks
training runs. No dataset is needed: the notebook makes up its own data.

| Notebook | What it does |
| --- | --- |
| `mlflow_basics` | Fits a straight line with gradient descent three times, with different learning rates and epochs, and logs each run to MLflow |

## What you'll see

The same model is trained three times. Each run logs its settings, its results
and a plot:

| Run | Learning rate | Epochs | Final MSE | Fitted line |
| --- | --- | --- | --- | --- |
| `too-slow` | 0.0001 | 100 | about 100 | y = 1.53x + 0.25 |
| `just-right` | 0.01 | 100 | about 4.0 | y = 3.15x + 1.03 |
| `more-epochs` | 0.01 | 1000 | about 3.8 | y = 3.02x + 1.88 |

The true line is y = 3x + 2.

## How to run it

1. **Set up once** (from the repository root), if you haven't already. This
   installs MLflow along with everything else:

   ```sh
   just setup
   ```

2. **Run the notebook.** Open `mlflow_basics.ipynb` in VS Code (kernel:
   `.venv`), or start JupyterLab with `just lab`, then run all cells. The
   three runs print their results at the end of step 4.

3. **Open the MLflow UI.** In a terminal, from this folder:

   ```sh
   cd playground/mlflow
   uv run mlflow ui --backend-store-uri sqlite:///mlflow.db
   ```

   Open <http://127.0.0.1:5000>, choose the `playground-linear-regression`
   experiment, tick the runs and click **Compare**:
   - the parameters side by side
   - the `mse` curve for each run on one chart
   - each run's `fit.png` plot under **Artifacts**

   Press Ctrl+C in the terminal to stop the UI.

4. **Experiment.** Change the values in `settings` (step 4 of the notebook)
   and run that cell again. New runs are added next to the old ones, so you
   can compare every attempt.

## Where the runs are saved

MLflow saves runs in this folder: the details in `mlflow.db` and the plots in
`mlruns/`. Git ignores both. To start from a clean slate, delete them.

The UI runs on your own computer only. In Binder the notebook runs as it is,
and step 5 shows the runs as a table, but the UI isn't available. Colab doesn't
come with MLflow: add a cell at the top with `!pip install -q mlflow` first.
