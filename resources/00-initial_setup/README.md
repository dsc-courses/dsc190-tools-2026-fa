# Initial Course Setup

## Set Up Your Linux Environment

In the first part of the course, we'll learn how to work in a Linux
environment. To start quickly, we'll use Docker to give everyone a consistent
Linux environment. Docker runs a lightweight container on your machine — think
of it as a small Linux computer running inside your computer.

### Step 0) Windows only: set up WSL

Mac users can skip this step.

Windows doesn't come with a Linux shell, so before continuing, follow **Steps 1
and 2** of [Setting up a UNIX environment on
Windows](../01-unix_on_windows/README.md) to install Ubuntu through WSL and
install `git`.

From then on, whenever these instructions (or lecture) say to use "your
terminal", Windows users should use the **Ubuntu** app, *not* PowerShell.

### Step 1) Install Docker Desktop

Download and install **Docker Desktop** for your operating system:

    https://www.docker.com/products/docker-desktop/

Follow the installer's instructions. Once installed, launch Docker Desktop and
make sure it's running (you should see the Docker icon in your menu bar or
system tray).

Note: On Windows, Docker Desktop works best with WSL2. During installation, make
sure the "Use WSL 2 instead of Hyper-V" option is selected. After installing,
open Docker Desktop's Settings, go to Resources → WSL Integration, and make
sure **Ubuntu** is switched on.

### Step 2) Start the container

Next, we'll start the Linux container by running a command in the *terminal*.
On macOS, use the built-in Terminal app. On Windows, use the Ubuntu app you set
up in Step 0.

First, open your terminal app and check that your terminal can talk to Docker
by running the following command:

    docker run hello-world

You should see a message starting with "Hello from Docker!". If you don't, see
[Troubleshooting](#troubleshooting) below.

We've made a *script* that starts the course's Linux container for you. It
lives in the course repository, so first download (*clone*) the repository
using git (a tool we will learn about in detail later in the quarter), then run
the script from inside it:

    git clone https://github.com/dsc-courses/dsc190-tools-2026-fa.git
    cd dsc190-tools-2026-fa
    bash start-linux.sh

On a Mac, the `git clone` command may ask you to install the "command line
developer tools". Say yes, wait for the install to finish (it takes a few
minutes), and then run the `git clone` command again.

You should now be inside a Linux shell, ready to go! This is the environment
we'll use for the first part of the quarter.

You only need to clone the repository once. Next time, just open your
terminal and run:

    cd dsc190-tools-2026-fa
    bash start-linux.sh

## Troubleshooting

| You see | Why | Fix |
|---|---|---|
| `bash` (or `bash.exe`) "is not recognized" | You're in PowerShell | Open the Ubuntu app instead (see Step 0) |
| `docker: command not found` (in Ubuntu) | Docker isn't connected to WSL | Turn on WSL Integration for Ubuntu (see Step 1), then close and reopen Ubuntu |
| "Cannot connect to the Docker daemon" | Docker Desktop isn't running | Start Docker Desktop and wait for it to finish starting |
| `git: command not found` (in Ubuntu) | `git` isn't installed | Run `sudo apt update && sudo apt install git` |
| `fatal: destination path 'dsc190-tools-2026-fa' already exists` | You've already cloned the repository | Skip the `git clone` step and just `cd` into it |
