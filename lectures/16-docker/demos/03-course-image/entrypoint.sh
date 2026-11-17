#!/bin/bash
set -e

# Initialize home directory on first run with a named volume
if [ ! -f "$HOME/.initialized" ]; then
    cp -a /etc/skel/. "$HOME"/
    git clone https://github.com/dsc-courses/dsc190-tools-2026-fa.git "$HOME/dsc190-tools-2026-fa"
    touch "$HOME/.initialized"
fi

# Configure opencode to ask before writing files or running commands
if [ ! -f "$HOME/.config/opencode/opencode.json" ]; then
    mkdir -p "$HOME/.config/opencode"
    cat > "$HOME/.config/opencode/opencode.json" << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "read": "allow",
    "grep": "allow",
    "glob": "allow",
    "list": "allow",
    "edit": "ask",
    "write": "ask",
    "apply_patch": "ask",
    "bash": {
      "*": "ask",
      "ls *": "allow",
      "grep *": "allow"
    }
  }
}
EOF
fi

# Update the tldr cache if it doesn't exist or is older than 30 days
if [ ! -d "$HOME/.cache/tealdeer" ] || \
   [ -z "$(find "$HOME/.cache/tealdeer" -maxdepth 0 -mtime -30 2>/dev/null)" ]; then
    tldr --update
fi

sudo /usr/sbin/sshd

exec /bin/bash --login
