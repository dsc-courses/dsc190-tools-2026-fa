# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy", "matplotlib"]
# ///
"""Draw a grid of example faces from utkcropped.npz.

Usage:
    uv run utkfaces.py <path to utkcropped.npz>

Writes utkfaces.png next to this script.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

faces = np.load(sys.argv[1])["faces"]
rng = np.random.default_rng(190)
idx = rng.choice(len(faces), size=12, replace=False)

fig, axes = plt.subplots(2, 6, figsize=(12, 4.4))
for ax, i in zip(axes.flat, idx):
    ax.imshow(faces[i].reshape(200, 200), cmap="gray", vmin=0, vmax=255)
    ax.axis("off")
fig.tight_layout(pad=0.3)
fig.savefig(Path(__file__).with_suffix(".png"), dpi=100, facecolor="white")
