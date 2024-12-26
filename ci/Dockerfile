FROM python:3.12-slim

RUN python3 -m pip install -U pip && pip install uv

WORKDIR /home/app/
COPY pyproject.toml uv.lock ./
RUN uv sync && rm pyproject.toml uv.lock

COPY src /home/app/src
COPY ci/entrypoint.sh /home/app/src/
WORKDIR /home/app/src

ENTRYPOINT ["./entrypoint.sh"]
