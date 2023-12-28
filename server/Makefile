.PHONY: help
help:		## list available cmds.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: build
build:				## build docker image to local registry
	docker build \
		-t ssa-py-api:local \
		-f docker/Dockerfile \
		.

# --no-cache \
.PHONY: build.dev
build.dev:			## build development docker image to local registry
	docker build \
		-t ssa-py-api:local-dev \
		-f docker/Dockerfile.dev \
		.

.PHONY: shell
shell: build.dev		## run local development docker container shell
	docker run --rm -it \
		--env-file .env \
		-v ${PWD}/src:/opt/app-root/src/src \
		-v ${PWD}/Pipfile:/opt/app-root/src/Pipfile \
		-v ${PWD}/docker/cmds/start_server.sh:/opt/app-root/src/start_server.sh \
		-p 0.0.0.0:8080:8080 \
		ssa-py-api:local-dev /bin/bash

.PHONY: run
run: build			## run local development docker container
	docker run --rm \
		-v ${PWD}/src:/opt/app-root/src \
		-p 0.0.0.0:8080:8080 \
		ssa-py-api:local
