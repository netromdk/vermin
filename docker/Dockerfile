# author: daniel rode


# https://docs.docker.com/reference/dockerfile/


FROM docker.io/python:3.14-alpine

# Install packages
RUN python3 -m pip install --root-user-action=ignore --no-cache-dir vermin

ENTRYPOINT ["/usr/local/bin/vermin"]
