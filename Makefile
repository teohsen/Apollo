# Define variables
DOCKER_IMAGE_NAME := bookmarkapp
DOCKER_IMAGE_TAG := latest
GIT_HASH := $(shell git rev-parse HEAD)

.PHONY: help build run stop clean

help:
	@echo "Available targets:"
	@echo "  build       - Build the Docker image"
	@echo "  run         - Run the Docker container"
	@echo "  stop        - Stop the Docker container"
	@echo "  clean       - Remove the Docker image and stop the container"

build:
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) . --build-arg GIT_HASH=$(GIT_HASH)

run:
	docker run -d -it -p 5000:5000 --name $(DOCKER_IMAGE_NAME) $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

stop:
	docker stop $(DOCKER_IMAGE_NAME)
	docker rm $(DOCKER_IMAGE_NAME)

clean: stop
	docker rmi $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
