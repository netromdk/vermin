#!/usr/bin/env bash
# author: daniel rode


# Build container
cd "$(dirname "$0")"
podman build --tag vermin .
