# build the manager binary
FROM golang:1.22 as builder

WORKDIR /workspace

# copy the go modules manifests
COPY go.mod go.mod
COPY go.sum go.sum

# cache deps before building and copying source so that we don't need to re-download as much
# and so that source changes don't invalidate our downloaded layer
RUN go mod download

# copy the go source
COPY cmd/ cmd/
COPY pkg/ pkg/

# build
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -o manager cmd/manager/main.go

# use distroless as minimal base image to package the manager binary
# Refer to https://github.com/googlecontainertools/distroless for more details
FROM registry.access.redhat.com/ubi9/ubi-minimal

WORKDIR /
COPY --from=builder /workspace/manager .
USER 65532:65532

ENTRYPOINT ["/manager"]
