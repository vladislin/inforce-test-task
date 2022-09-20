FROM python:3.9

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.13 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# System deps:
RUN  pip install "poetry==$POETRY_VERSION" && poetry --version

# set work directory
WORKDIR /app

# Install dependencies:
COPY ../ pyproject.toml poetry.lock /app/
RUN poetry install
# copy project
COPY .. .