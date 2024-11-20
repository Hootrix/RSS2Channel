# FROM python:3.9-slim as python-deps 
# 和distroless中py版本不一致会导致python环境找不到，除非手动指定为distroless中的目前 11 版本
# https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile

FROM debian:12-slim AS python-deps
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# 设置工作目录
WORKDIR /app
COPY Pipfile .
# COPY Pipfile.lock .
RUN /venv/bin/pip install pipenv && PIPENV_VENV_IN_PROJECT=1 /venv/bin/pipenv install --deploy


FROM gcr.io/distroless/python3-debian12
COPY --from=python-deps /app/.venv/ /venv
COPY . /app
WORKDIR /app
ENTRYPOINT ["/venv/bin/python3", "main.py"]