# Setting up a UNIX environment on MacOS

UNIX/Linux is the standard environment for data science and software
development, and so you'll want to be able to run such an environment on your
own computer. If you have a Mac, you're in luck -- macOS is based on UNIX[^1].
This means that there is only a little bit of setup required.

## Step 1: Install Homebrew

We have seen that Linux distributions come with command-line package managers
(Debian's is called `apt`). macOS doesn't, but there is a very popular
third-party package manager called Homebrew. Homebrew allows us to easily install the tools
we need for this class, and it also provides a convenient way to manage updates.

To install Homebrew, you'll run a command in your terminal that downloads the
installer script and runs it with bash. The install command is found on the
front page of the Homebrew website: https://brew.sh/.

Homebrew works by manipulating the `PATH` environment variable, as we discussed
in lecture. To check that it is installed correctly, run `brew --version` in
your terminal. If you see the version number, then Homebrew is installed and
ready to use.

## Step 2: Install `git`

One of the most important tools we'll cover in this class is `git`, which is a version control system.

macOS already comes with `git` installed, but it is an older version. To get
the latest version, you can install it with Homebrew. Run the following command in your terminal:

```bash
brew install git
```

Then check that it is installed correctly by running:

```
type -a git
```

You should see several locations, with the top one being the Homebrew version (probably something like `/opt/homebrew/bin/git`).

## Step 3 (Optional): Make it nice

Next, you might want to install some more modern tools to make your experience
nicer (and the nicer your experience, the more you'll reach for these tools). This,
however, is totally optional.

### A new terminal (Ghostty)

First, you might want to install a nicer terminal app than the one that comes
with macOS. I recommend Ghostty, which provides modern features like tabs,
clickable links, lots of colors, and ligatures (fancy fonts). It is also very
fast. Install it with Homebrew:

```bash
brew install --cask ghostty
```

### A better shell (Fish)

The default shell on macOS is `zsh`, which is a more feature-rich version of
the `bash` shell. However, there is an even more modern shell called `fish`
that has many nice features like better autocompletion and syntax highlighting.
Using it is highly recommended, as it makes it easier to use the command line.

It can be installed with Homebrew, too:

```bash
brew install fish
```

To use the Fish shell, you can run the `fish` command in your terminal.
However, to make it your default, we recommend updating your terminal's
settings. First, run `type fish` and note the path of the `fish` executable.
Then, open your terminal's settings and find a place to specify the default
shell or the command that is run on start. In Ghostty, this is done by
pressing `Cmd + ,` to open settings, then finding (or adding) a line starting
with `Command = ...`. Change this to point to your `fish` executable, e.g.,

```
Command = /opt/homebrew/bin/fish
```

### A better prompt (Starship)

The _prompt_ is the text that is shown before your cursor in the terminal. By
default, it contains your username, the computer's name, and the current
directory. However, there are many modern prompts that show much more
information, like the current git status, the status of your Python virtual
environment, and more. One of the most popular is called
[Starship](https://starship.rs). Install it with Homebrew:

```bash
brew install starship
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
install. Most are available with Homebrew. Here are a few that we use:

- `fd`: a modern replacement for `find`. Install with `brew install fd`.
- `rg`: a modern replacement for `grep`. Install with `brew install ripgrep`.
- `bat`: a modern replacement for `less`. Install with `brew install bat`.
- `lsd`: a modern replacement for `ls`. Install with `brew install lsd`.

If you install `lsd`, you might also want to add an alias to your shell
configuration file (e.g., `~/.config/fish/config.fish` for Fish) to make it run
when you type `ls`. The below will configure your shell so that `ls`
automatically prints in list form, grouping directories first. It will also
create a `tree` command that shows a directory tree.

```fish
alias ls='command lsd -l --group-dirs first'
alias tree='command lsd --tree --group-dirs first --no-symlink'
```

[^1]:
    In fact MacOS is based on FreeBSD, which itself was based on BSD
    (Berkeley Software Distribution), which was a flavor of UNIX developed at
    UCB.
