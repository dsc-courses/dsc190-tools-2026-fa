# Why Docker

- What can a Docker environment specify that a Python virtual environment (like `venv`) cannot?
    - **Answer**: Non-Python software dependencies, such as a database server or a web server.

# Images and containers

- What is a Docker image?
    - **Answer**: A frozen snapshot of an operating system and installed software.

- What is a Docker container?
    - **Answer**: A running instance of an image.

# Dockerfiles

- What is a Dockerfile?
    - **Answer**: A file that specifies the steps to build a Docker image.

- Which Dockerfile directive specifies the base image?
    - **Answer**: `FROM`.

- Which Dockerfile directive specifies the default command to run when a container starts?
    - **Answer**: `CMD`.

- What is the difference between `RUN` and `CMD` in a Dockerfile?
    - **Answer**: `RUN` executes a command while the image is being built; `CMD` is the command run when a container starts.

# Building and managing images

- What command builds an image named `my-image` from the Dockerfile in the current directory?
    - **Answer**: `docker build -t my-image .`

- In `docker build -t my-image path/to/dir`, what is `path/to/dir`?
    - **Answer**: The directory containing the Dockerfile (the build context).

- Why should you avoid putting large files in the directory you pass to `docker build`?
    - **Answer**: All files in that directory are copied into the build context.

- What command lists the images on your system?
    - **Answer**: `docker image ls`.

# Layers

- What does each instruction in a Dockerfile create?
    - **Answer**: A new filesystem layer.

- When you rebuild an image after changing one instruction in its Dockerfile, which instructions are re-run?
    - **Answer**: The changed instruction and every instruction after it; earlier layers come from the cache.

- Why should you install dependencies before copying your source code in a Dockerfile?
    - **Answer**: Otherwise every code change invalidates the cached dependency-install layer, so dependencies are reinstalled on every build.

- Why pin the versions of base images and packages in a Dockerfile?
    - **Answer**: For reproducible builds.

# Running containers

- What command creates and runs a container from the image `my-image`?
    - **Answer**: `docker run my-image`.

- When you `docker run` an image without giving a command, what does the container run?
    - **Answer**: The command specified by `CMD` in the Dockerfile.

- What flags do you pass to `docker run` to run a container interactively, e.g., to get a shell?
    - **Answer**: `-it`.

- What command lists the running containers?
    - **Answer**: `docker ps`.

- What does the `--rm` flag to `docker run` do?
    - **Answer**: Removes the container automatically when it stops.

# Volumes

- What happens to a file that you create inside of a container when the container is removed?
    - **Answer**: It is lost.

- What Docker feature lets you persist data across container runs?
    - **Answer**: Volumes.

- What is a bind mount?
    - **Answer**: A volume that maps a specific directory on the host into the container.

- What is a named volume?
    - **Answer**: A volume whose storage location Docker manages, rather than a specific host directory.

- What does `docker run -v /path/on/host:/path/in/container my-image` do?
    - **Answer**: Runs `my-image` with the host directory `/path/on/host` mounted at `/path/in/container`, so the container can read and write it.
