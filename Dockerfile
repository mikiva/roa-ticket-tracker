from node:latest as SPA_BUILDER
WORKDIR /app
COPY frontend/package*.json .
RUN CI=false npm install
COPY frontend/ .

RUN npm run build

FROM python:3.10

RUN pip install "poetry==1.1.12"
WORKDIR /roa
COPY backend/poetry.lock backend/pyproject.toml /roa/

RUN poetry config virtualenvs.create false \
&& poetry install --no-dev --no-interaction --no-ansi

COPY backend/ .

COPY --from=SPA_BUILDER /app/dist/ /app/spa



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]