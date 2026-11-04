# Git and large files

- Why is git not well-suited for tracking large binary files like image datasets or PyTorch model weights?
    - **Answer**: Git's compression and diffing do not work well on binary files, so the repo grows large and slow.

- What does DVC do?
    - **Answer**: It tracks large files efficiently by storing them outside the git repo.

# Setting up DVC

- What command initializes DVC inside an existing git repo?
    - **Answer**: `dvc init`.

- What directory does `dvc init` create to hold DVC configuration and metadata?
    - **Answer**: `.dvc/`.

- What file does `dvc init` create that works like `.gitignore` but for DVC?
    - **Answer**: `.dvcignore`.

- Where does `dvc init` put DVC's configuration file?
    - **Answer**: `.dvc/config`.

# Adding files

- What command tells DVC to start tracking a file named `utkcropped.npz`?
    - **Answer**: `dvc add utkcropped.npz`.

- What file is created when you run `dvc add utkcropped.npz`?
    - **Answer**: `utkcropped.npz.dvc`, a metadata file describing the tracked file.

- What is stored in the `utkcropped.npz.dvc` file?
    - **Answer**: Metadata about the file, including its md5 hash, size, and path.

- What does `dvc add utkcropped.npz` do to `.gitignore`?
    - **Answer**: It adds `utkcropped.npz` to `.gitignore` so that git ignores the actual data file.

- After running `dvc add utkcropped.npz`, which files should be committed to git?
    - **Answer**: `utkcropped.npz.dvc` and the updated `.gitignore`, but not `utkcropped.npz` itself.

- After `dvc add utkcropped.npz`, where is the actual data file tracked: by git or by DVC?
    - **Answer**: By DVC; git only tracks the small `.dvc` metadata file.

# DVC remotes

- What command adds a DVC remote?
    - **Answer**: `dvc remote add`

- What command uploads tracked data files to the DVC remote?
    - **Answer**: `dvc push`.

- Does `dvc push` also push your git commits to the git remote?
    - **Answer**: No; you must run `git push` separately.

# Pulling and checking out data

- A coworker just cloned the repo. What command downloads the actual data files from the DVC remote?
    - **Answer**: `dvc pull`.

- After running `git switch` to an older commit, why is the data file not automatically updated?
    - **Answer**: Git only tracks the `.dvc` metadata file, so the actual data must be fetched separately with DVC.

- What command downloads the version of the data referenced by the current git commit?
    - **Answer**: `dvc pull`.

- What is the difference between `dvc pull` and `dvc checkout`?
    - **Answer**: `dvc pull` downloads data from the remote, while `dvc checkout` only copies it from the local DVC cache.

- After updating a tracked dataset, what is the correct sequence of commands to publish the change?
    - **Answer**: `dvc add` the file, `git commit` the updated `.dvc` files, then `dvc push` and `git push`.

# Data pipelines

- What command defines a new stage of a DVC pipeline?
    - **Answer**: `dvc stage add`.

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-n` flag specify?
    - **Answer**: The name of the stage (`clean`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-d` flag specify?
    - **Answer**: A dependency of the stage (the input file `data/raw.csv`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-o` flag specify?
    - **Answer**: An output of the stage (the file `data/clean.csv`).

- What command runs the pipeline defined in `dvc.yaml`?
    - **Answer**: `dvc repro`.

