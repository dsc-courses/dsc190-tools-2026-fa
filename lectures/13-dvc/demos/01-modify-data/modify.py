# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy"]
# ///
"""Make a small change to utkcropped.npz, in place.

Usage:
    uv run modify.py [path]

Overwrites 100 random pixels of the faces array in `path` (default:
utkcropped.npz in the current directory) and saves it uncompressed. Run it
between commits to simulate receiving a new version of the data.
"""

import sys

import numpy as np

N_PIXELS = 100

path = sys.argv[1] if len(sys.argv) > 1 else "utkcropped.npz"

faces = np.load(path)["faces"]

rng = np.random.default_rng()
idx = rng.integers(0, faces.size, size=N_PIXELS)
faces.flat[idx] = rng.integers(0, 256, size=N_PIXELS, dtype=np.uint8)

np.savez(path, faces=faces)
print(f"Changed {N_PIXELS} pixels in {path}")
