"""Evaluate model predictions and generate summary statistics."""

import json
import pandas as pd


def evaluate(predictions_path, metrics_path):
    preds = pd.read_csv(predictions_path)
    with open(metrics_path) as f:
        metrics = json.load(f)

    print(f"Accuracy: {metrics['accuracy']:.3f}")
    print(f"Training samples: {metrics['n_train']}")
    print(f"Prediction distribution:\n{preds['prediction'].value_counts()}")


if __name__ == "__main__":
    evaluate("results/model_v1/predictions.csv", "results/model_v1/metrics.json")
