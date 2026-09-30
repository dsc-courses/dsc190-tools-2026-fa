"""Shared utility functions."""

import os


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def row_count(csv_path):
    with open(csv_path) as f:
        return sum(1 for _ in f) - 1  # subtract header
