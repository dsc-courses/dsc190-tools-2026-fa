# start from an official image that already has Python and uv installed
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# all subsequent commands run from /app inside the container
WORKDIR /app

# install dependencies first. this layer is cached and only rebuilt when the
# lockfile changes, so code edits don't trigger a slow reinstall.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

# copy the application code and the trained model into the image
COPY app.py model.pkl ./

# document that the API listens on port 8000
EXPOSE 8000

# serve the API in production mode. --host 0.0.0.0 makes it reachable from
# outside the container (not just from localhost inside it).
CMD ["uv", "run", "fastapi", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
