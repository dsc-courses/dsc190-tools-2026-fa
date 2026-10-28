# Assignment 05: GitHub Actions and Pre-commit Hooks

**Due**: Tuesday, November 3 at 11:59 PM on Gradescope

In lecture, we saw a common git workflow for team projects: keep `main` clean,
do your work on feature branches, and merge changes via pull requests. The
point of this extra step (the pull request) is to provide an opportunity to
collaboratively check the quality of the code before it goes into `main`.

We also saw how to use `ruff` to lint and format code. Tools like `ruff`
provide *automatic* ways to check the quality of your code. Ideally, we'd run
these tools regularly so that sloppy code never makes it into `main`, but it's
easy to forget.

As it turns out, there are ways to automatically run the linter and formatter.
This assignment will introduce you to two of them: GitHub Actions and
pre-commit hooks. Along the way, you'll get practice with the pull request
workflow and with managing Python environments and dependencies with `uv`.

**What to turn in**: this assignment is a guided tour of GitHub Actions and
pre-commit hooks. As you go through the steps below, you'll create a public
GitHub repository and configure it with the workflows described above. At the
end, you'll submit the URL of the repo to Gradescope. The autograder will check
that the repo is public and contains the expected files, pull requests, and
commit history.

## Step 0: Set up your GitHub account and SSH keys

In this assignment, you'll be creating a public GitHub repository. In order to
do this, you will first need to create a GitHub account if you don't already have one.

Moreover, to push changes to GitHub from your local machine, you will need to
authenticate somehow (otherwise *anyone* could make changes to your repo!).
Once upon a time, Git allowed users to authenticate with a username and
password. Not only was this a pain (you had to enter your password every time
you pushed), but it was also insecure. Nowadays, you *must* set up SSH (secure
shell) keys to authenticate with GitHub.

> While this is probably not the time or place for a full explanation of SSH
> and public-key cryptography, the basic idea is this: you generate a pair of
> keys on your local machine, consisting of a *private* key (which you keep
> secret and *never* share with anyone) and a *public* key (which you can share
> freely). These keys can be used to *encrypt* a message. The private and the
> public keys are mathematically linked, so that if you encrypt a message with
> the public key, it can only be decrypted with the private key. When you set
> up your public key on GitHub, GitHub uses the public key to encrypt a random
> message and sends it to your machine. If you have the private key, you can
> decrypt the message and send it back to GitHub, which proves that you are the
> owner of the keys and allows you to authenticate. If you *don't*, you can't
> decrypt the message and authentication fails. Not only is it very secure, it
> is very convenient, since you never have to type a password.

If you've ever used GitHub before, you may have already set up your SSH keys. If
not, follow the
[instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)
in the GitHub docs.

## Step 1: Create a public repo on GitHub

Head to <https://github.com/new> and create a new repository:

- Give it any name you want
- Make sure that the visibility is **Public**.
- Check the box to **Add a README file**. (This ensures the repo has at least
  one commit and a `main` branch right out of the gate, which we'll need for
  the next step.)
- Leave the rest of the options at their defaults, and click **Create
  repository**.

You should see a fresh repository with a single `README.md` file and one
branch, `main`.

## Step 2: Protect the `main` branch

In many projects, the `main` branch should always be "clean" (e.g., the code
should always be runnable and correct). Merging code into `main` should be a
deliberate and careful act. To enforce this, projects will often set up *branch
protection rules* that prevent anyone from pushing directly to `main` and
require all changes to go through pull requests.

In your new repo:

1. Click the **Settings** tab (near the top of the page).
2. In the left sidebar, click **Branches**.
3. Under "Branch protection rules", click **Add branch ruleset**.
4. Give the ruleset a name (e.g., "Protect main") 
5. Set the "Enforcement status" to Active.
6. Under "Target branches", include the default branch.
7. Under the "Branch rules", some rules will automatically be checked (that's
   OK). However, make sure to check **Require a pull request before merging**.
   This option has many sub-options, but you can leave them all unchecked for
   this assignment.

## Step 3: Set up the project with `uv`

Now we'll set up a Python project inside the repo using `uv`.

First, clone your git repo to your local machine. You can find the URL to clone
on the main page of your repo, under the green "Code" button. It should look
like: `git@github.com:<your-username>/<your-repo-name>.git`

While in a shell inside the cloned repo, initialize a new `uv` project at the
root of the repo (that is, the `pyproject.toml` should be at the top level of
your git repository, and not in a subdirectory). Then, using `uv`, add `numpy`
as a runtime dependency and `ruff` as a dev dependency. Then commit these
changes (along with all of the files created by `uv init`) to the main branch.

We want to push these changes to GitHub, but because of the branch protection
rule we just set up, we can't push directly to `main`. (Go ahead and try: you
should see an error message).

Instead, create a feature branch, and push that branch to your public repo.
Open a pull request to merge it into `main` as we did in lecture. Then, on
GitHub merge the pull request. Once it's done, delete the feature branch both
on GitHub and locally.

Back on your local machine, the `main` branch is now out of sync with GitHub.
Pull the latest version of GitHub's `main` and delete the feature branch.

*Note*: This process of creating a pull request might seem like a lot of
ceremony for making such a small change. In fact, it *is* overkill if you're
the only person working on the project. In the "real world", you'll be working
on a team, and you usually won't be approving your own pull requests: one of
your colleagues will give them a "peer review" and approve them.

## Step 4: Add a GitHub Action to run the linter

We'd like to make sure that all code that goes into `main` passes `ruff check`.
To run `ruff check` on every pull request, we can set up a **GitHub Action**.

A **GitHub Action** is a workflow that runs automatically on GitHub's servers
when something happens in your repo — for example, when someone pushes a commit
or opens a pull request. The workflow can do anything you can do in a shell:
install dependencies, run tests, build documentation, deploy a site, and so on.

We're going to set up an action that runs `ruff check` on every push to `main`
and every pull request targeting `main`. That way, code that doesn't pass
`ruff` won't make it into `main`.

Workflows are defined in YAML files inside the `.github/workflows/` directory
at the root of the repo. Create a new feature branch named `add-lint-workflow`,
then create the file `.github/workflows/lint.yml` with the following contents:

```yaml
name: Lint

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: astral-sh/setup-uv@v10.3.2
      - run: uv sync
      - run: uv run ruff check
```

Let's break this down:

- `name`: a human-readable name for the workflow.
- `on`: the events that trigger the workflow. Here, we trigger on pushes to
  `main` and on pull requests targeting `main`.
- `jobs`: the work the workflow does. We define a single job named `lint`.
- `runs-on`: the kind of virtual machine to run the job on. `ubuntu-latest` is
  the standard choice.
- `steps`: the individual steps the job runs.
    - `uses: actions/checkout@v7` invokes a pre-made action named "checkout"
      that checks out a fresh copy of your repo.
    - `uses: astral-sh/setup-uv@v10.3.2` is another pre-made action that installs
      `uv` into the Ubuntu environment. 
    - `run: uv sync` literally runs `uv sync` in the Ubuntu virtual machine,
      within the checked-out copy of your repo. This creates a virtual
      environment from `pyproject.toml` and `uv.lock`.
    - `run: uv run ruff check` runs the linter inside the venv.

> **Tip**: you can find the latest version of any action by visiting its
> GitHub page (e.g., <https://github.com/actions/checkout> or
> <https://github.com/astral-sh/setup-uv>) and looking at the **Releases**.

Commit the workflow file and push the branch. Then open a pull request from
`add-lint-workflow` into `main`. As soon as the PR is open, the workflow should
start running. You can watch it in real time by clicking the **Actions** tab on
GitHub, or by scrolling down to the "checks" section at the bottom of the PR.

The check should pass (the `main.py` that `uv init` created has no lint
errors). Once it does, merge the PR and clean up the branch as before.

## Step 5: Require the action to pass before merging

Right now, the action runs, but a failing action wouldn't actually block a
merge. Let's fix that.

Go back to your repository's settings, but this time find the "Rules" section
on the left, and go to the "Rulesets" page. You should see the branch ruleset
you created in Step 2. Click on it, and find the "Require status checks to
pass" option and check it. Then click the "Add checks" button and select the
`lint` check from the dropdown (you might need to search for it to get it to
appear). Save your changes by clicking the big green button at the bottom of
the page.

Now any pull request that fails the `lint` check will be blocked from merging.

## Step 6: Watch the protection in action

Time to test it. Back on your machine, update the `main` branch by pulling the
latest changes from GitHub. Then create a new feature branch named
`break-things`. As the name implies, we're going to break things in this branch
and see how the lint check prevents us from merging the broken code into
`main`.

Open `main.py` and modify it to violate **at least three different ruff
rules**. You can find a list of all of the things that `ruff` checks for in the
[documentation](https://docs.astral.sh/ruff/rules/).

Before pushing, try running `ruff check` to verify that three rules are
broken. But don't fix them! Instead, commit and push, then open a new pull
request to merge them into `main`. The `lint` check should run and **fail**.
With the branch protection rule from Step 5 in place, the **Merge pull
request** button should be disabled.

On the PR page, you will only see that the check failed, but you won't see the
details of the lint errors. To see those, click on the check (it should be
named "Lint / lint (pull_request)" or similar). This will take you to the page
for that workflow run. One of the steps should have failed, indicated by a red
circle with an "X" inside. Expand that step to see the output of the `ruff
check` command, which will include the lint errors.

*Note*. You might be wondering: how can GitHub know if the `ruff check`
succeeded or failed? Is it parsing the output of the command to look for words
like "fail" or "error"? No, it's actually much simpler than that: every Unix
process returns an *exit code* when it finishes. By convention, an exit code of
`0` means the process succeeded, and any non-zero exit code means it failed.
When you run `uv run ruff check` on the faulty `main.py`, it returns a non-zero
exit code, which tells GitHub that the check failed.

## Step 7: Fix the errors and merge

Back on your local machine, fix the lint errors in `main.py`. Commit these to
the same `break-things` branch and push. This will automatically update the
pull request you already created and will trigger the `lint` check to run
again. This time, it should pass. With the check passing, the **Merge pull
request** button will become enabled. Merge the PR, delete the branch, and pull
the latest `main` back to your local repo as before.

What we have set up here with GitHub actions is called a **continuous
integration (CI) pipeline**. CI is a software development practice in which
developers frequently integrate their code into a shared repository, and each
integration is automatically verified by running tests, linters, and other
checks. This helps catch errors early and ensures that the codebase remains
healthy.

## Step 8: Set up a pre-commit hook

A failing CI run is annoying. It would be nicer to catch problems *before* we
push to GitHub. That's where **pre-commit hooks** come in: scripts that run
automatically every time you run `git commit`.

Git supports hooks natively, but the most popular way to manage them is with
the [pre-commit](https://pre-commit.com) tool. It is written in Python, so
we can install it with `uv`. Add it as a dev dependency to our project.

```bash
uv add --dev pre-commit
```

Pre-commit looks for a configuration file named `.pre-commit-config.yaml` at
the root of your repo. This file contains a list of the hooks that should be
run on each commit. You can find the available hooks in the [pre-commit
registry](https://pre-commit.com/hooks.html). For now, we'll use two of the
hooks provided by the `ruff`
[package](https://github.com/astral-sh/ruff-pre-commit).

Following the [instructions](https://github.com/astral-sh/ruff-pre-commit),
set up the `check` and `format` hooks in your `.pre-commit-config.yaml` file.
Don't enable automatic lint fixes.

Once that is done, install the hook into your local `.git/` directory:

```bash
uv run pre-commit install
```

You should see a message that pre-commit was installed at
`.git/hooks/pre-commit`.

Let's try it out. Edit `main.py` to introduce some formatting issues. A simple
one is to leave out spaces around an operator, like this:

```python
x=1+2
```

Now try to commit `main.py`. You should see something like:

```text
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook

1 file reformatted
```

The commit will have **failed** — but if you check `main.py`, you'll see that
it has been automatically reformatted. This is the standard pre-commit
workflow: the hook modifies your files in place and aborts the commit so you
can inspect the changes. To finish the commit, just stage the formatted file
and commit again:

```bash
git add main.py
git commit -m "Test pre-commit"
```

This time the hook will have nothing to do and the commit will go through.

## Step 9: Commit the pre-commit configuration

The hook itself was installed locally (in `.git/`, which isn't tracked), but
the config file should be checked into the repo so that anyone who clones it
can install the same hook with one command.

Create a new feature branch with the `.pre-commit-config.yaml` file and commit
it (along with all other changed project files). Then push it to GitHub and
open a pull request to merge it into `main`. The `lint` check should pass.
Merge the PR and delete the branch.

## What to turn in

Submit to Gradescope a single file named `repo_url.txt` containing a single
line with the URL of your GitHub repository. The autograder will:

- verify that the repo is public and accessible,
- check that the expected files (`pyproject.toml`, `uv.lock`,
  `.github/workflows/lint.yml`, `.pre-commit-config.yaml`) are present on
  `main`,
- inspect the commit history to confirm that you went through the PR
  workflow described above.

All of the autograder tests are public.
