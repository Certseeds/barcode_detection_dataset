#!/usr/bin/env bash
set -euox pipefail
main(){
  podman \
    build \
    -f "$(pwd)"/containerfile \
    --ignorefile "$(pwd)"/containerignore \
    --log-level warn \
    .
}
main
