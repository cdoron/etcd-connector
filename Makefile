DOCKER_HOSTNAME ?= ghcr.io

DOCKER_NAMESPACE ?= cdoron

DOCKER_TAG ?= 0.0.0

DOCKER_NAME ?= etcd-connector

IMG := ${DOCKER_HOSTNAME}/${DOCKER_NAMESPACE}/${DOCKER_NAME}:${DOCKER_TAG}

export HELM_EXPERIMENTAL_OCI=1

all: build

.PHONY: build
build:
	cd swagger-datacatalog; docker build . -t ${IMG}; cd ..

.PHONY: docker-push
docker-push:
	docker push ${IMG}

.PHONY: push-to-kind
push-to-kind:
	kind load docker-image ${IMG}
