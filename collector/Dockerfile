FROM python:3.10-buster as py-builder

WORKDIR /app
USER root
RUN apt install curl -y

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
COPY . /app
ENV PATH=/opt/poetry/bin:$PATH
RUN poetry config virtualenvs.in-project true && poetry install

FROM python:3.10-slim-buster

COPY --from=py-builder /app /app


USER 1001
WORKDIR /app
CMD /app/.venv/bin/python /app/main.py