# Dockerfile describes how exactly we build the Docker container. It contains instructions for building the image, such as which base image to use, which files to copy, and which commands to run.

# 1. What we base our image on
FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code 
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked 


COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]
