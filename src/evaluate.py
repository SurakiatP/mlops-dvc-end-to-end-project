# src/evaluate.py
import sys
import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from dvclive import Live
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def evaluate(model_path, input_csv, output_json):
    model = joblib.load(model_path)
    df = pd.read_csv(input_csv)

    if "target" not in df.columns:
        raise ValueError("Missing 'target' column in features")

    X = df.drop(columns=["target"])
    y_true = df["target"]

    y_pred = model.predict(X)

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    metrics = {
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1_score": f1
    }

    # Log evaluation metrics using DVCLive; ใช้ report="html" แทน "auto"
    with Live("../02_experiment_tracking", report="md") as live:
        live.log_metric("eval_accuracy", acc)
        live.log_metric("eval_precision", prec)
        live.log_metric("eval_recall", rec)
        live.log_metric("eval_f1", f1)
        live.next_step()

    with open(output_json, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"✅ Metrics saved to {output_json}")
    print(metrics)

    cm = confusion_matrix(y_true, y_pred)
    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("../02_experiment_tracking/plots/confusion_matrix.png")


if __name__ == "__main__":
    model_path = sys.argv[1]
    input_csv = sys.argv[2]
    output_json = sys.argv[3]
    evaluate(model_path, input_csv, output_json)
