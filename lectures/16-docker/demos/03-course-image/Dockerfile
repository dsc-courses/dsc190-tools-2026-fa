# Start from Debian Linux as our base image. This gives us a minimal Linux
# system to build on top of.
FROM debian:bookworm

# Install useful command-line tools using apt-get, Debian's package manager.
# "update" refreshes the list of available packages, and "install -y" installs
# them without prompting for confirmation.
RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    bat \
    bash \
    coreutils \
    curl \
    file \
    fish \
    fd-find \
    fzf \
    ripgrep \
    findutils \
    grep \
    gzip \
    less \
    man-db \
    nano \
    net-tools \
    procps \
    sed \
    tar \
    tree \
    vim \
    wget \
    git \
    jq \
    zoxide \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/sshd

# Some Debian packages install under different names to avoid conflicts with
# existing commands. These symlinks let us use the more common names.
RUN ln -s /usr/bin/fdfind /usr/bin/fd \
    && ln -s /usr/bin/batcat /usr/bin/bat

# Install tealdeer (tldr client) from GitHub releases, since the Debian
# bookworm package is very outdated. Pick the right binary for the architecture.
RUN ARCH=$(dpkg --print-architecture) \
    && case "$ARCH" in \
         amd64) TLDR_ARCH="x86_64" ;; \
         arm64) TLDR_ARCH="aarch64" ;; \
         *) echo "Unsupported architecture: $ARCH" && exit 1 ;; \
       esac \
    && curl -fsSL "https://github.com/tealdeer-rs/tealdeer/releases/latest/download/tealdeer-linux-${TLDR_ARCH}-musl" -o /usr/local/bin/tldr \
    && chmod +x /usr/local/bin/tldr

# Create a non-root user called "student". The -m flag creates a home
# directory, and -s sets their default shell to bash.
# We also add them to the sudo group so they can run commands as root.
RUN useradd -m -s /bin/bash student \
    && echo "student:student" | chpasswd \
    && echo "student ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install opencode, an AI-powered coding assistant. The installer puts it in
# /root/.opencode/bin, so we move it to /usr/local/bin to make it available
# system-wide.
RUN curl -fsSL https://opencode.ai/install | bash \
    && mv /root/.opencode/bin/opencode /usr/local/bin/opencode

# these are "extra" packages that we didn't know (or forgot) to add in the
# original package list early in the quarter, and we're adding them here to
# prevent a rebuild of the image's early layers. in a future quarter, these
# should be merged into the earlier apt-get install command.
RUN apt-get update && apt-get install -y \
    lsd \
    python3.11-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy our custom entrypoint script into the container and make it executable.
COPY --chmod=755 entrypoint.sh /entrypoint.sh

# Expose SSH port
EXPOSE 22

# Switch to the student user so we're not running as root.
USER student
WORKDIR /home/student

# Copy custom shell helpers into /etc/profile.d/ so they are available in all
# login shells, even when the home directory is a mounted volume.
COPY profile/ /etc/profile.d/

# Copy the WELCOME file into the student's home directory.
COPY --chown=student:student WELCOME /home/student/WELCOME

# ENTRYPOINT defines the command that runs when the container starts.
ENTRYPOINT ["/entrypoint.sh"]
