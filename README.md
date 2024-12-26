# simple personal page
![version](https://img.shields.io/badge/version-0.1.0-brightgreen)
![python](https://img.shields.io/badge/python-3.12-brightgreen)

## dependencies

- docker
- docker compose

## how to

### prod-like run

1. clone the repo
1. put the ssl cert and it's key in `ci/certs`; [letsencrypt](https://letsencrypt.org) is easiest way to get them
1. put the `.env` file in the `ci` folder and fill it out; see `ci/.env.example`
1. build the docker image: `docker build . -t personal-page-app -f ci/Dockerfile`
1. create docker volumes:
    - `docker create volume page-db`
    - `docker create volume page-static-files`
    - `docker create volume page-media-files`
1. run the application: `docker compose -f ci/docker-compose.yaml up -d`

### development

1. clone the repo
1. install `uv` package manager: `python3 -m pip install -U pip && pip install uv`
1. sync project dependencies: `uv sync`
1. init the db (sqlite by default): `uv run python3 manage.py migrate`
1. run dev server: `uv run python3 manage.py runserver`
