FROM python:3.10-slim-buster

LABEL maintainer="Amogh Madan <amoghmadaan@gmail.com>"

WORKDIR /quick_contact

RUN python3 -m pip install poetry

COPY ./pyproject.toml /quick_contact/
COPY ./poetry.lock /quick_contact/

RUN poetry install --with=production
