---
theme:
  path: ../../.presenterm/theme.yaml
  override:
    footer:
      style: template
      right: "{current_slide} / {total_slides}"
options:
  list_item_newlines: 2
---


Working Remotely
================

To follow along, clone the course repo:

```bash
git clone https://github.com/dsc-courses/dsc190-tools-2026-fa.git
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Working Remotely</span>**

Working Remotely
================

- We have so far been working within a development environment that is local to our machines.
- But you will sometimes need to work *remotely* on a **server**.
    - E.g., to run a long-running analysis or one that requires more computational resources than your local machine has.
    - E.g., to work with protected data that is stored on a server.
    - E.g., to deploy/configure a web application.

SSH
===

- The most common way to work remotely on a server is via **SSH** (Secure Shell).
- Allows you to log in remotely and run a shell on a Linux/Unix server.

```bash
ssh username@hostname
```


Example
=======

- You all have accounts on UCSD's *Data Science and Machine Learning* (DSML) server.
- To log in, run:

```bash
ssh <your-username>@dsmlp-login.ucsd.edu
```

- Your username is your UCSD username (e.g., `jeldridge`).
- Your password is your ActiveDirectory password.

Note
====

- This is just the DSMLP login server -- don't run any analyses here!

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">SSH Keys</span>**

SSH Keys
========

- Authenticating with a password is not ideal.
    - It is annoying.
    - It is less secure (can be brute-forced).
- Instead, use **SSH keys**.


How SSH Keys Work
=================

- You will generate two *keys*.
- A **private key** that you keep on your local machine.
    - *Never* let this key leave your machine.
- A **public key** that you upload to the server.
    - This key can be shared freely.
- **Key Fact**: A message that is encrypted with the *public* key can only be
  decrypted with the *private* key.

How SSH Keys Work
=================

You try to log in to a server.

1. The server (which has your public key) generates a random message (think: a secret word) and encrypts it with your public key.
2. The server sends the encrypted message to your local machine.
3. Your local machine decrypts the message with your private key and sends it back to the server.
4. The server checks that the decrypted message (secret word) is the same as the original. If so, authentication is successful.

Generating SSH Keys
===================

- To generate keys, run:

```bash
ssh-keygen
```

- **Note**: you don't need to do this if you already have SSH keys.
- This creates two files in `~/.ssh/`:
    - private key: `id_ed25519` (or `id_rsa`)
    - public key: `id_ed25519.pub` (or `id_rsa.pub`)

Public Keys are *Public*
========================

- You can share them freely.
- In fact, GitHub *publishes* your public key when you add it to your GitHub account.

`https://github.com/<your-username>.keys`

Private Keys are *Private*
==========================

- If someone gets access to your private key, they can log in as you to any
  server that has your public key.

Copying Public Keys to Servers
==============================

- To copy your public key to a server, run:

```bash
ssh-copy-id username@hostname
```

- This modifies the `~/.ssh/authorized_keys` file on the server to include your public key.

Demo
====

- Copy your public key to the DSMLP server:

```bash
ssh-copy-id <your-username>@dsmlp-login.ucsd.edu
```

SSH Keys and Agents
===================

- Sometimes you'll want an agent to do something on a remote server via SSH.
- Agents will often refuse to type your password for you.
- But they will happily use your SSH keys to log in.

How many keys?
==============

- You can generate as many keypairs as you want.
- You can use different keys for different servers.
- But for simplicity, most people just generate one key per machine and use it for all servers.

Why?
====

- What is the *threat model*?
- Different keys for different servers *seems* more secure.
- But in what situation will an attacker get access to one of your private keys but not the others?

Example
=======

- Your laptop is stolen and the thief is able to login.
- All of your private keys are files in `~/.ssh/` on your laptop.
- So the thief gets access to all of your private keys, not just one.

(This is one reason why it is important to have your disks encrypted and to have a strong password on your laptop.)

Aside
=====

- Journalists will often use PGP keypairs to allow sources to send them encrypted messages.

![image:w:50%](./fig/journalist.png)


---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">SSH Config</span>**

SSH Config
==========

- The SSH configuration file lives at `~/.ssh/config`.
- In particular, it allows you to set up *aliases* for servers so that you
  don't have to type the full username and hostname every time.

Syntax
======

```bash
Host dsmlp
    HostName dsmlp-login.ucsd.edu
    User <your-username>
```

Demo
====

Add the previous to your SSH config and run:

```bash
ssh dsmlp
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Copying Files</span>**

Copying Files
=============

- Suppose you need to copy a file from your local machine to the server.
- How?

Approach #1: scp
================

- `scp` (secure copy) is a command for copying files to/from servers over SSH.

```bash
scp local_file username@hostname:remote_file
```

SCP
===

- scp behaves like `cp` (e.g., you can use `-r` to copy directories).
- Uses SSH under the hood.
    - Works with SSH keys auth and your SSH config.

Approach #2: rsync
==================

- `rsync` is a more powerful command for *syncing* files to/from servers over SSH.
1. Can detect which files have changed and only copy those.
2. Can resume interrupted transfers.
3. Can do more complex syncing (e.g., delete files on the destination that are not on the source).

rsync
=====

To copy a directory from your local machine to the server, run:

```bash
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose
# -z: compress file data during the transfer
rsync -avz local_dir/ username@hostname:remote_dir
```

rsync
=====

To *sync* a directory (make the remote directory look exactly like the local directory), run:

```bash
# --delete: delete files on the destination that are not on the source
rsync -avz --delete local_dir/ username@hostname:remote_dir
```

Approach #3: Use Git Push+Pull
==============================

- To sync project code, a common pattern is to use Git push and pull.
1. Set up a Git remote (e.g., on GitHub).
2. Modify the code on your local machine, commit, and push to GitHub.
3. Log in to the server and git pull the latest code from GitHub.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Running Long Processes</span>**

Running Long Processes
======================

- Sometimes you'll want to run a long process on a server.
    - E.g., training a model that takes 12 hours.
- <span class="bad">**Problem**</span>: when you close your SSH connection, the
  process is killed.
- You don't want to need to keep your computer on and connected to the internet
  for 12 hours just to train a model.

Solution: screen / tmux
=======================

- screen and tmux are <span class="term">**terminal multiplexers**</span>
- They allow you to create a long-lived "virtual" terminal that you can attach/detach from.
    - Also allow you to make splits/tabs.
- You can start a process in a screen/tmux session, detach, and log out. The process will keep running.

tmux
====

- Run "tmux" to start a tmux session.
- "Ctrl-b" is the "prefix" key for tmux commands.
- Press "Ctrl-b" then "?" to see a list of commands.
- Press "Ctrl-b" then "d" to detach from the session.
- To re-attach to the session, run "tmux attach".

Agents
======

- Sometimes, you'll want to start an agent on a server.
    - E.g., to let the agent work while your laptop is off.
- You can do this with screen/tmux.
- Alternatively, new tools designed specifically for running agents are appearing.
    - E.g., <span class="term">**herdr**</span>

herdr
=====

- "Tmux for agents"
- Lets you start lots of agents (maybe on a server), detach, and re-attach later.
- Makes it easier to find which agents need you.
- Has a mobile app (so you can work anywhere!)

<span class="bad">**Warning!**</span>
========

- You can run long jobs on DSMLP, but there's a separate process!
- *Don't* just log in via SSH and run a long process.
- Instead, follow these instructions: https://support.ucsd.edu/its?id=kb_article&sys_id=4d9c45dd1b96495448e9cae5604bcb0b


