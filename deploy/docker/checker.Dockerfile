FROM python:3.12-slim


WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH="${PYTHONPATH}:/project/app"

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry install
COPY app app

CMD ["python", "app/external/checker.py"]