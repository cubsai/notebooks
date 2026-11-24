# %% [markdown]
# # MLflow basics: tracking three training runs
#
# This notebook trains the same tiny model three times with different
# settings, and uses MLflow to record each run so you can compare them.
#
# - **The model:** a straight line, `y = w * x + b`, fitted with gradient
#   descent (the method from ML Week 2).
# - **The data:** made up in the notebook, so there's nothing to download.
#   The true line is `y = 3x + 2`, plus some random noise.
# - **What MLflow records for each run:** the settings we chose (parameters),
#   the results (metrics, including the loss after every epoch), and a plot
#   (an artifact).

# %%
import matplotlib.pyplot as plt
import mlflow
import numpy as np

# %% [markdown]
# ## 1. Tell MLflow where to save runs
#
# Runs are saved in a small database file, `mlflow.db`, next to this notebook
# (git ignores it). An *experiment* is a named group of runs.

# %%
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("playground-linear-regression")

# %% [markdown]
# ## 2. Make some data
#
# 100 points along the line `y = 3x + 2`, with random noise added.
# The seed makes the "random" numbers the same every time you run it.

# %%
rng = np.random.default_rng(seed=42)
x = rng.uniform(0, 10, size=100)
y = 3 * x + 2 + rng.normal(0, 2, size=100)

plt.scatter(x, y, s=10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Our made-up data")
plt.show()


# %% [markdown]
# ## 3. The training function
#
# Gradient descent starts with `w = 0` and `b = 0`, then nudges both a little
# on every epoch to reduce the mean squared error (MSE).
#
# The two settings we'll change:
#
# - `learning_rate`: how big each nudge is.
# - `epochs`: how many nudges.


# %%
def train(x, y, learning_rate, epochs):
    """Fit y = w*x + b with gradient descent. Returns w, b and the loss per epoch."""
    w, b = 0.0, 0.0
    losses = []
    for _ in range(epochs):
        error = (w * x + b) - y
        losses.append(float(np.mean(error**2)))
        w -= learning_rate * 2 * np.mean(error * x)
        b -= learning_rate * 2 * np.mean(error)
    return w, b, losses


# %% [markdown]
# ## 4. Three runs, three sets of settings
#
# Each `with mlflow.start_run():` block is one run. Inside it we log:
#
# - **parameters** (`log_params`): the settings for this run
# - **metrics** (`log_metric`): the loss at every epoch, so MLflow can draw
#   the curve, plus the final results
# - **an artifact** (`log_figure`): a plot of the fitted line

# %%
settings = [
    {"run_name": "too-slow", "learning_rate": 0.0001, "epochs": 100},
    {"run_name": "just-right", "learning_rate": 0.01, "epochs": 100},
    {"run_name": "more-epochs", "learning_rate": 0.01, "epochs": 1000},
]

for s in settings:
    with mlflow.start_run(run_name=s["run_name"]):
        mlflow.log_params({"learning_rate": s["learning_rate"], "epochs": s["epochs"]})

        w, b, losses = train(x, y, s["learning_rate"], s["epochs"])

        for epoch, loss in enumerate(losses):
            mlflow.log_metric("mse", loss, step=epoch)
        mlflow.log_metrics({"final_mse": losses[-1], "w": w, "b": b})

        fig, ax = plt.subplots()
        ax.scatter(x, y, s=10, label="data")
        xs = np.linspace(0, 10, 50)
        ax.plot(xs, w * xs + b, color="red", label=f"fit: y = {w:.2f}x + {b:.2f}")
        ax.set_title(s["run_name"])
        ax.legend()
        mlflow.log_figure(fig, "fit.png")
        plt.close(fig)

        print(f"{s['run_name']:12} final MSE {losses[-1]:7.2f}   w = {w:.2f}   b = {b:.2f}")

# %% [markdown]
# ## 5. Compare the runs
#
# The true line is `y = 3x + 2`, and the noise alone gives an MSE of about 4.
#
# - **too-slow** (learning rate 0.0001): the nudges are tiny, so after 100
#   epochs the line is still far too flat (`w` about 1.5). MSE about 100.
# - **just-right** (learning rate 0.01): bigger nudges get the slope right in
#   the same 100 epochs, but `b` is still low (about 1). MSE about 4.0.
# - **more-epochs** (learning rate 0.01, 1000 epochs): more time lets `b`
#   settle too, giving the line closest to `y = 3x + 2`. MSE about 3.8.
#
# You can also read the runs back as a table, without opening the UI:

# %%
runs = mlflow.search_runs(experiment_names=["playground-linear-regression"])
runs[["tags.mlflow.runName", "params.learning_rate", "params.epochs", "metrics.final_mse", "metrics.w", "metrics.b"]]

# %% [markdown]
# ## 6. Open the MLflow UI
#
# In a terminal, from this folder, run:
#
# ```
# uv run mlflow ui --backend-store-uri sqlite:///mlflow.db
# ```
#
# Then open http://127.0.0.1:5000, choose the
# `playground-linear-regression` experiment, tick the three runs and click
# **Compare**. You'll see the parameters side by side, the `mse` curves on one
# chart, and each run's `fit.png` under **Artifacts**.
#
# Each time you re-run step 4, three new runs are added, so you can change
# the settings and compare against earlier attempts.
