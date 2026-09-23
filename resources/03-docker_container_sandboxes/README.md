# Using Docker Containers as Agent Sandboxes

In [Picking an AI Subscription](https://github.com/dsc-courses/dsc190-tools-2026-fa/blob/main/resources/02-picking_an_ai/README.md), it was suggested
to use Docker Sandboxes (`sbx`) to contain your coding agent. Docker Sandboxes
are a new feature, and they aren't compatible with older operating systems
(Windows 10 and macOS pre-Tahoe). This note walks you through an alternative
that uses plain Docker containers. Docker containers are not quite as secure as
Docker Sandboxes, but they are good enough for practical purposes.

You should already have Docker installed from before.

## Installing the `sandbox-agent` script

The [`sandbox-agent`](https://github.com/dsc-courses/dsc190-tools-2026-fa/blob/main/resources/03-docker_container_sandboxes/sandbox-agent) script in this directory is what you'll
run to launch an agent. To use it from any directory, you need to put it
somewhere on your `PATH`. To do so:

1. Open the Terminal (in WSL if you're on Windows).
2. Create a `~/bin` directory if you don't already have one:

   ```bash
   mkdir -p ~/bin
   ```

3. Download `sandbox-agent` into `~/bin` and make it executable:

   ```bash
   curl -fsSL -o ~/bin/sandbox-agent \
       https://raw.githubusercontent.com/dsc-courses/dsc190-tools-2026-fa/main/resources/03-docker_container_sandboxes/sandbox-agent
   chmod +x ~/bin/sandbox-agent
   ```

4. Add `~/bin` to your `PATH` if it isn't already by modifying `~/.profile` (or
   whatever the appropriate startup file is for your shell).

5. Verify the script works by running:

   ```bash
   which sandbox-agent
   sandbox-agent --help
   ```

## Using `sandbox-agent`

`cd` into the project directory you want the agent to work in, then run one
of:

```bash
sandbox-agent claude
sandbox-agent codex
sandbox-agent opencode
```

The first time you run each agent, the container image will be pulled from
GitHub Container Registry (a few hundred MB, one-time cost per agent), and
you'll need to log in using the agent's built-in flow (e.g. `/login` for
`claude`, `codex login` for `codex`, or opencode's auth menu). Credentials are
stored in a per-agent Docker volume (`dsc190-agent-sandbox-<agent>-home`) and
reused on later runs, so you only have to log in once per agent.

To fetch the latest image on a subsequent run, pass `--pull`:

```bash
sandbox-agent claude --pull
```

Your sandbox will be isolated from your main machine, however, the agent will
be able to read and modify *anything* and *everything* under the directory that
it is created in. Moreover, the agent has been pre-configured to not require
permission to run commands, write to files, etc. It also has unrestricted
access to the internet. Giving this amount of freedom to the agent is
permissible *because* it is sandboxed.
