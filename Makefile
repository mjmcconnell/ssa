.PHONY: help
help:		## list available cmds.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: build
build:				## build docker image to local registry
	docker build \
		-t fm:local \
		-f docker/Dockerfile \
		.
