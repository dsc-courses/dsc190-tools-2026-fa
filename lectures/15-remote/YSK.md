# SSH basics

- What does the command `ssh username@hostname` do?
    - **Answer**: Logs in remotely and starts a shell on the server `hostname` as `username`.

- What does SSH stand for?
    - **Answer**: Secure Shell.

- What command would you run to log in to UCSD's DSMLP server as user `jeldridge`?
    - **Answer**: `ssh jeldridge@dsmlp-login.ucsd.edu`.

# SSH keys

- In SSH key authentication, which key do you keep on your local machine?
    - **Answer**: The private key.

- In SSH key authentication, which key do you put on the server?
    - **Answer**: The public key.

- What is the key cryptographic fact that makes SSH key authentication work?
    - **Answer**: A message encrypted with the public key can only be decrypted with the private key.

- During SSH key authentication, what does the server do first?
    - **Answer**: It generates a random message, encrypts it with your public key, and sends it to your machine.

- During SSH key authentication, what does your local machine do with the encrypted message from the server?
    - **Answer**: It decrypts the message with your private key and sends it back to the server.

- How does the server decide that SSH key authentication has succeeded?
    - **Answer**: It checks that the decrypted message it receives back matches the original random message.

- What command generates a new SSH keypair?
    - **Answer**: `ssh-keygen`.

- In what directory does `ssh-keygen` place the generated keys by default?
    - **Answer**: `~/.ssh/`.

- After running `ssh-keygen` with the `ed25519` algorithm, what is the filename of the private key?
    - **Answer**: `id_ed25519`.

- After running `ssh-keygen` with the `ed25519` algorithm, what is the filename of the public key?
    - **Answer**: `id_ed25519.pub`.

# Copying public keys to a server

- What command copies your public SSH key to a server so you can log in without a password?
    - **Answer**: `ssh-copy-id username@hostname`.

- What file on the server does `ssh-copy-id` modify?
    - **Answer**: `~/.ssh/authorized_keys`.

# SSH config

- Where does the SSH client look for its configuration file?
    - **Answer**: `~/.ssh/config`.

- What is the main convenience that `~/.ssh/config` provides?
    - **Answer**: It lets you define aliases for servers so you don't have to type the full username and hostname every time.

# scp

- What does `scp local_file username@hostname:remote_file` do?
    - **Answer**: Copies `local_file` from your local machine to `remote_file` on the server, using SSH.

- What flag does `scp` use to copy a directory recursively?
    - **Answer**: `-r`.

# rsync

- What is the main advantage of `rsync` over `scp` when copying files that have been copied before?
    - **Answer**: `rsync` detects which files have changed and copies only those.

- What happens if an `rsync` transfer is interrupted partway through?
    - **Answer**: It can be resumed from where it left off.

- In `rsync -avz local_dir/ username@hostname:remote_dir`, what does the `-a` flag do?
    - **Answer**: Enables archive mode, which preserves permissions, timestamps, and other file attributes.

- In `rsync -avz local_dir/ username@hostname:remote_dir`, what does the `-v` flag do?
    - **Answer**: Enables verbose output.

- In `rsync -avz local_dir/ username@hostname:remote_dir`, what does the `-z` flag do?
    - **Answer**: Compresses file data during the transfer.

- What does the `--delete` flag do in `rsync -avz --delete local_dir/ username@hostname:remote_dir`?
    - **Answer**: Deletes files on the destination that no longer exist on the source.

# Long-running processes

- What happens by default to a process you started over SSH when you close the SSH connection?
    - **Answer**: The process is killed.

- What kind of tool are `screen` and `tmux`?
    - **Answer**: Terminal multiplexers.

- What problem do terminal multiplexers like `tmux` solve for remote work?
    - **Answer**: They let you start a long-running process, detach from the session, log out, and have the process keep running.

- What key combination detaches you from a `tmux` session?
    - **Answer**: `Ctrl-b` then `d`.

- What command reattaches you to a previously detached `tmux` session?
    - **Answer**: `tmux attach` (or `tmux att` for short.)
