FROM tiangolo/uvicorn-gunicorn-fastapi:latest
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.2.0
WORKDIR /code
# Install Poetry
RUN apt-get update && apt-get install libsndfile1 -y \
    python3.9 \
    python3-pip 
RUN pip install poetry

COPY app/pyproject.toml app/poetry.lock* /code/
# Allow installing dev dependencies to run tests
# RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
#RUN pip install google-cloud-speech
ENV PYTHONPATH=/code
EXPOSE 8000