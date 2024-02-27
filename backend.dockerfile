FROM python:3.9-slim

COPY backend/ app/
WORKDIR /app

ENV PYTHONUNBUFFERED True
ENV ENVIRONMENT PRODUCTION
ENV DEBUG false

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-dev && \
    rm -rf /root/.cache

COPY backend/pyproject.toml backend/poetry.lock /app/

ENV PORT 8080
ENV PATH="${PATH}:/app/.venv/bin"

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
