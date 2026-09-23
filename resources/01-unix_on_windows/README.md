# Setting up a UNIX environment on Windows

UNIX/Linux is the standard environment for data science and software
development, and so you'll want to be able to run such an environment on your
own computer. Windows is not based on UNIX, but Microsoft provides an official
way to run a real Linux environment alongside Windows called the **Windows
Subsystem for Linux** (WSL). Once it is set up, you'll have a full Ubuntu Linux
system accessible from your Windows machine, and most of the rest of this
class will work just like it does on macOS or Linux.

## Step 1: Install WSL

*Note*: you may have already installed WSL when installing Docker. If so, you
can skip this step.

Open PowerShell as an Administrator (right-click the Start menu, search for
PowerShell, and choose "Windows PowerShell (Admin)"). Then run:

```powershell
wsl --install
```

This installs WSL and, by default, the latest Ubuntu distribution. When it
finishes, restart your computer.

After rebooting, launch "Ubuntu" from the Start menu. The first time you run
it, it will finish setting up and ask you to create a UNIX username and
password. This account is separate from your Windows account -- pick something
short and memorable, and remember the password, since you'll need it when
running commands with `sudo`.

From here on, whenever these notes (or lecture) say to "run something in your
terminal", you should run it inside this Ubuntu shell, *not* in PowerShell or
`cmd.exe`. Ubuntu is a real Linux environment, so commands like `ls`, `cat`,
and `apt` all work as expected.

To check that things are working, run:

```bash
uname -a
```

You should see output mentioning `Linux` and `Ubuntu`.

## Step 2: Update packages and install `git`

Ubuntu comes with the same command-line package manager as Debian: `apt`.
Before installing anything, it's a good idea to update the list of available
packages and upgrade the system:

```bash
sudo apt update
sudo apt upgrade
```

One of the most important tools we'll cover in this class is `git`. Ubuntu
usually comes with `git` already, but to make sure you have it (and the latest
version from Ubuntu's repositories), run:

```bash
sudo apt install git
```

Then check that it is installed correctly:

```bash
type -a git
git --version
```

You should see `git` located at `/usr/bin/git`.

## Step 3 (Optional): Make it nice

Next, you might want to install some more modern tools to make your experience
nicer (and the nicer your experience, the more you'll reach for these tools).
This, however, is totally optional.

### A new terminal (Windows Terminal)

If you're on Windows 11, the built-in **Windows Terminal** app is already quite
good. It should be installed by default on Windows 11; if you're using Windows
10, get it from the Microsoft Store. When you open Windows Terminal, click the
down-arrow next to the tab bar and choose "Ubuntu" to open a WSL tab. You can
also set Ubuntu as the default profile in Settings.

### A better shell (Fish)

The default shell in Ubuntu is `bash`. However, there is a more modern shell
called `fish` that has many nice features like better autocompletion and syntax
highlighting. Using it is highly recommended, as it makes it easier to use the
command line.

Install it with `apt`:

```bash
sudo apt install fish
```

To use the Fish shell, you can run the `fish` command in your terminal. To make
it your default shell, first run `type fish` and note the path of the `fish`
executable (probably `/usr/bin/fish`). Then run:

```bash
chsh -s /usr/bin/fish
```

Close and reopen your terminal; `fish` should now start automatically.

### A better prompt (Starship)

The _prompt_ is the text that is shown before your cursor in the terminal. By
default, it contains your username, the computer's name, and the current
directory. However, there are many modern prompts that show much more
information, like the current git status, the status of your Python virtual
environment, and more. One of the most popular is called
[Starship](https://starship.rs). Install it with:

```bash
curl -sS https://starship.rs/install.sh | sh
```

You might also need to follow the setup instructions listed at the [Starship
install guide](https://starship.rs/guide/). For example, to install Starship
into the Fish shell, you must add the following to the end of
`~/.config/fish/config.fish`:

```fish
starship init fish | source
```

### Better miscellaneous tools (fd, rg, etc.)

There are also many other modern command-line tools that you might want to
install. Most are available with `apt`. Here are a few that we use:

- `fd`: a modern replacement for `find`. Install with `sudo apt install fd-find`. On Ubuntu, the binary is called `fdfind`; you may want to add an alias `alias fd='fdfind'`.
- `rg`: a modern replacement for `grep`. Install with `sudo apt install ripgrep`.
- `bat`: a modern replacement for `less`. Install with `sudo apt install bat`. On Ubuntu, the binary is called `batcat`; you may want to add an alias `alias bat='batcat'`; see below for an example of adding an alias.
- `lsd`: a modern replacement for `ls`. Install with `sudo apt install lsd`.

If you install `lsd`, you might also want to add an alias to your shell
configuration file (e.g., `~/.config/fish/config.fish` for Fish) to make it run
when you type `ls`. The below will configure your shell so that `ls`
automatically prints in list form, grouping directories first. It will also
create a `tree` command that shows a directory tree.

```fish
alias ls='command lsd -l --group-dirs first'
alias tree='command lsd --tree --group-dirs first --no-symlink'
```

## A note on files and editors

Your WSL Ubuntu system has its own filesystem, separate from Windows. Your
Linux home directory lives at `/home/<your-unix-username>` inside WSL, and you
can also reach it from Windows at `\\wsl$\Ubuntu\home\<your-unix-username>`.
Your Windows drives are mounted inside WSL at `/mnt/c`, `/mnt/d`, etc.

For best performance, keep the files you work on for this class *inside* the
Linux filesystem (i.e., somewhere under `/home/...`) rather than on `/mnt/c`.

If you use VS Code, install the ["WSL"
extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
and then, from inside your Ubuntu shell, run `code .` in any project
directory. VS Code will launch on Windows but edit, run, and debug your code
inside Linux.
