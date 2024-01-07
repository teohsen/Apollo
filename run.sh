#!/bin/bash

# Fetch the latest Git commit hash
GIT_HASH=$(git rev-parse HEAD)
SERVICE_NAME=bookmarkapp

# Check if Git hash is empty
if [ -z "$GIT_HASH" ]; then
  echo "Failed to fetch Git commit hash. Exiting."
  exit 1
fi

# Run Docker with the Git hash as an argument
docker build -t $SERVICE_NAME:latest . --build-arg GIT_HASH=$GIT_HASH
