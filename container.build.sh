#!/usr/bin/env bash
set -euox pipefail
main(){
  podman \
    build \
    -f "$(pwd)"/Containerfile \
    --ignorefile "$(pwd)"/.containerignore \
    --log-level warn \
    ,
}
main
