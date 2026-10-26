- Why is it a bad idea to commit large non-text files (e.g., PDFs, images, datasets) to a Git repo?
    - **Answer**: Git stores a copy of every version of every file, so they consume lots of space and slow down operations like `git status`.

- What is the name of the file used to tell Git which files to ignore?
    - **Answer**: `.gitignore`

- Where in the project is the `.gitignore` file usually placed?
    - **Answer**: At the root of the project.

- In a `.gitignore` file, what does the line `*.pdf` do?
    - **Answer**: Tells Git to ignore all files whose names end in `.pdf`.

- According to the recommended solo workflow, what state should the `main` branch always be in?
    - **Answer**: A "clean" state — e.g., the code should run without errors.

- According to the recommended solo workflow, where should new work be done?
    - **Answer**: On a new feature branch, not directly on `main`.

- What is a "feature branch"?
    - **Answer**: A branch created for a single task, feature, or experiment, separate from `main`.

- What does a "squash merge" do?
    - **Answer**: Combines all the commits from a branch into a single commit on the target branch.

- What command performs a squash merge of the branch `feature` into the current branch?
    - **Answer**: `git merge --squash feature`

- After running `git merge --squash feature`, what step is required to actually record the merge?
    - **Answer**: Run `git commit` to create the squashed commit.

- After squash-merging a branch `feature` into `main`, what command deletes the `feature` branch?
    - **Answer**: `git branch -D feature`

- In GitHub Flow, how is a feature branch merged into `main`?
    - **Answer**: By opening a pull request on GitHub and merging it there.

- After committing changes to a local feature branch, what must you do before opening a pull request?
    - **Answer**: Push the branch to GitHub.

- What Git feature lets several AI agents work on the same repository in parallel, each on its own branch in its own directory?
    - **Answer**: Worktrees (`git worktree`).
