# src/train.py
import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from dvclive import Live
import yaml


def train_model(input_csv, output_model):
    # Load params from YAML
    with open("../params.yaml", "r") as f:
        params = yaml.safe_load(f)["train"]

    model_type = params["model_type"]
    max_iter = params["max_iter"]

    df = pd.read_csv(input_csv)
    if "target" not in df.columns:
        raise ValueError("Missing 'target' column. Please run featurize first.")

    X = df.drop(columns=["target"])
    y = df["target"]

    # Create model
    if model_type == "LogisticRegression":
        model = LogisticRegression(max_iter=max_iter)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    model.fit(X, y)

    # Calculate training accuracy
    y_pred = model.predict(X)
    train_acc = accuracy_score(y, y_pred)

    # Log metric to DVCLive
    with Live("../02_experiment_tracking", report="md") as live:
        live.log_metric("train_accuracy", train_acc)
        live.next_step()

    joblib.dump(model, output_model)
    print(f"✅ Model saved to {output_model}")


if __name__ == "__main__":
    input_csv = sys.argv[1]
    output_model = sys.argv[2]
    train_model(input_csv, output_model)
