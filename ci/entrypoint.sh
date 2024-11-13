#!/bin/bash

set -ex

uv run python3 manage.py migrate
uv run python3 manage.py collectstatic --no-input --clear

exec "$@"
