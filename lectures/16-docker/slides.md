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


Docker
======

To follow along, clone the course repo:

```bash
git clone https://github.com/dsc-courses/dsc190-tools-2026-fa.git
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Docker</span>**

Virtual Environments
====================

- We have seen Python *virtual environments* (e.g., `venv`).
- These allow us to specify the Python packages that are needed for a project.
- But what if a project also needs other *non-Python* software (e.g., a database, a web server, etc.)?

Docker
======

- *Docker* is a tool that allows us to define "virtual environments" that can include any software dependencies.
- E.g., we can specify that a project needs:
    - Python 3.10
    - DB Server: PostgreSQL 15
    - Web Server: Nginx 1.24
    - Key-Value Store: Redis 7

Use Cases
=========

1. Reproducible development environments.
2. Deploying applications to production servers.
3. Isolation and sandboxing.


Docker Vocabulary
=================

- **Image**: A frozen snapshot of an operating system and installed software.
- **Container**: A running "live" instance of an image.
    - Can have multiple running containers of the same image.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Defining Docker Images</span>**

Defining Docker Images
======================

- Many times, you'll get Docker images from others (e.g., from Docker Hub).
- Sometimes, you'll want to define your own.
- You do this with a *Dockerfile* that specifies the steps to build the image.

Example Dockerfile
==================

See: `demos/01-hello/Dockerfile`

```docker
# the "base" image
FROM ubuntu:24.04

# run commands to modify the files contained in the image
RUN apt-get update && apt-get install -y cowsay

# the command to run when a container starts
CMD ["/usr/games/cowsay", "Hello from Docker!"]
```

A More Realistic Example
========================

See: `demos/02-jupyter-pdf/Dockerfile`

```docker
FROM python:3.12-slim

# pip compiles `pdftotext` (a wrapper around poppler's
# C++ library) from source, so we need a C++ toolchain
# and the poppler-cpp headers
RUN apt-get update && apt-get install -y \
        build-essential \
        pkg-config \
        libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pdftotext pandas
```

Common Directives
=================

- `FROM`: specify the base image.
- `RUN`: execute a command during the build (e.g., install packages).
- `COPY`: copy files from the host into the image.
- `WORKDIR`: set the working directory for subsequent instructions.
- `ENV`: set an environment variable inside the image.
- `EXPOSE`: declare a port that the container will listen on.
- `CMD`: specify the default command to run when a container starts.

Common Base Images
==================

- `ubuntu` / `debian`: generic Linux distributions.
- `python`: official Python images (e.g., `python:3.12-slim`).
- `node`: Node.js runtime.
- `postgres`: PostgreSQL database server.
- `nginx`: web server.
- `redis`: in-memory key-value store.
- `nvidia/cuda`: CUDA base for GPU work.

Building Images
===============

- To build an image from a Dockerfile, run:
```bash
docker build -t my-image path/to/dir
```
- `path/to/dir` is the directory containing the Dockerfile.
- Note: all files in that directory are copied into the build context, so avoid putting large files there.

Layers
======

- Each instruction in a Dockerfile creates a new *filesystem layer*.
- An image is a stack of layers built one on top of the next.
- Docker *caches* each layer: rebuilding only re-runs the instructions that changed (and everything after them).
- Layers are shared across images, so a common base costs no extra disk space.

Working with Layers
===================

- **Order matters.** Put stable instructions (e.g., installing system packages) early; put frequently-changing ones (e.g., copying source code) late.
- **Install dependencies before copying code.** Otherwise every code change invalidates the dependency-install layer.
- **Combine related `RUN` commands.** Each `RUN` is its own layer; chain steps with `&&` and clean up in the same layer (e.g., `rm -rf /var/lib/apt/lists/*`).
- **Pin versions** of base images and packages for reproducible builds.

Listing Images
==============

- To list the images on your system, run:
```bash
docker image ls
```

Removing Images
===============

- To remove an image, run:
```bash
docker image rm <image-name>
# or
docker rmi <image-name>
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Running Containers</span>**

Containers
==========

- An image is a snapshot of a filesystem; a *container* is a running instance of that image.
- To create and run a container, run:
```bash
docker run <image-name>
```

- By default, the container runs the command specified by `CMD` in the Dockerfile.

Interactive Containers
======================

- To run a container interactively (e.g., to get a shell), use the `-it` flags:
```bash
docker run -it <image-name> /bin/bash
```

Listing Containers
==================

- To see all running containers, run:
```bash
docker ps
```

To Stop and Remove Containers
=============================

- To stop a running container, run:
```bash
docker stop <container-id>
```

- To remove a stopped container, run:
```bash
docker rm <container-id>
```

Automatic Cleanup
=================

- To remove a container immediately after it stops, use the `--rm` flag:
```bash
docker run --rm <image-name>
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Volumes</span>**

Docker Data
===========

- Docker images are *read-only* snapshots of a filesystem.
- This means, any changes you make inside of a container (e.g., creating files, installing packages, etc.) are lost when the container is removed, and a new `docker run` always starts from the unchanged image.
- To persist data across container runs, we can use *volumes*.

Volumes
=======

- Docker provides two types of volumes for persisting data:
    - **Bind mounts**: map a specific directory on the host into the container.
    - **Named volumes**: not a specific host directory; Docker manages the storage location.

Bind Mounts
===========

- To allow a host directory to be read/written by a container, use the `-v` flag:
```bash
docker run -v /path/on/host:/path/in/container <image-name>
```
- The directory on the host should exist before running the command.

Named Volumes
=============

- To create a named volume, run:
```bash
docker run -v <my-volume-name>:/path/in/container <image-name>
```
- The named volume will automatically be created if it doesn't exist.

