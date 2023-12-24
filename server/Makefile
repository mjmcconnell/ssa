.PHONY: help
help:		## list available cmds.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: docker.build
docker.build:		## build docker image to local registry
	docker build \
		-t ssa-py-api:local \
		-f docker/Dockerfile \
		.

.PHONY: docker.shell
docker.shell:		## run local docker container shell
	docker run --rm -it ssa-py-api:local /bin/bash
