# Initial Course Setup

## Install Docker

In the first part of the course, we'll learn how to work in a Linux
environment. To start quickly, we'll use Docker to give everyone a consistent
Linux environment. Docker runs a lightweight container on your machine — think
of it as a small Linux computer running inside your computer.

### Step 1) Install Docker Desktop

Download and install **Docker Desktop** for your operating system:

    https://www.docker.com/products/docker-desktop/

Follow the installer's instructions. Once installed, launch Docker Desktop and
make sure it's running (you should see the Docker icon in your menu bar or
system tray).

Note: On Windows, Docker Desktop works best with WSL2. During installation, make
sure the "Use WSL 2 instead of Hyper-V" option is selected.

### Step 2) Start the container

Next, we'll start the Linux container by running a command in the *terminal*.

Both Windows and Mac come with terminal applications -- on Windows, you can use
PowerShell, and on macOS you can use the built-in Terminal app. Open your
terminal and run:

    docker run -it --rm -v dsc190-tools-starter-home:/home/student ghcr.io/dsc-courses/dsc190-tools-starter

You should now be inside a Linux shell, ready to go! This is the environment
we'll use for the first part of the quarter.

The above is a lot to type, so we've made a *script* that executes that command
for you. You can download it at:

    https://github.com/dsc-courses/dsc190-tools-2026-fa/raw/main/start-linux.sh

Make note of where is was saved. Then, in your terminal, navigate to that
directory using the
[cd command](https://www.geeksforgeeks.org/linux-unix/cd-command-in-linux-with-examples/) and run:

    bash start-linux.sh
