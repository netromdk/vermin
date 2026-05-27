#!/usr/bin/env bash
# author: daniel rode


podman run \
    --rm \
    --interactive --tty \
    --volume "$PWD:$PWD" \
    --workdir "$PWD" \
    vermin \
    "$@" \
;
