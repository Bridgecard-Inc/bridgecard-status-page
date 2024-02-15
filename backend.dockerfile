FROM python:3.9
COPY backend/ app/
WORKDIR /app
RUN apt-get update
ENV PYTHONUNBUFFERED True
ENV ENVIRONMENT PRODUCTION
ENV DEBUG: true

RUN pip install poetry 

RUN poetry config virtualenvs.create false 

COPY backend/pyproject.toml backend/poetry.lock /app/

RUN poetry install --no-interaction

RUN export PYTHONPATH="."

ENV PORT 8080

EXPOSE 8080

ENV PATH="${PATH}:/app/.venv/bin"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
