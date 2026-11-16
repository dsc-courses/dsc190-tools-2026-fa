FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
        build-essential \
        pkg-config \
        libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pdftotext pandas

# default command is python
