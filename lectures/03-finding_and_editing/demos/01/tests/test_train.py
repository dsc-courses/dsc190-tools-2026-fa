"""Tests for model training pipeline."""

import json
import os


def test_metrics_file_exists():
    assert os.path.exists("results/model_v1/metrics.json")


def test_metrics_has_accuracy():
    with open("results/model_v1/metrics.json") as f:
        metrics = json.load(f)
    assert "accuracy" in metrics
    assert 0 <= metrics["accuracy"] <= 1
