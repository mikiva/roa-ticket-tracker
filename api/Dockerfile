FROM python:3.10.11-alpine as py-builder

WORKDIR /app
RUN apk --no-cache add curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
COPY . /app
ENV PATH=/opt/poetry/bin:$PATH
RUN poetry config virtualenvs.in-project true && poetry install

FROM python:3.10.11-alpine

COPY --from=py-builder /app /app

WORKDIR /app
CMD /app/.venv/bin/python /app/serve.py