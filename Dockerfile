# Stage 1: Build
FROM python:3.11-slim-bullseye as builder

WORKDIR /app
RUN apt-get update

COPY ./requirements.txt ./requirements.txt

RUN python -m venv /venv && . /venv/bin/activate && \
    pip install -r requirements.txt --no-cache-dir

COPY bookmark.py ./bookmark.py
COPY .env ./.env

# Stage 2: Run
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /venv /venv

ARG GIT_HASH
ENV GIT_HASH=$GIT_HASH

ENTRYPOINT ["/venv/bin/python", "bookmark.py"]
