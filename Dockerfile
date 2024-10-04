FROM python:3.12 AS base

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"
# Disable Poetry's virtual environment
RUN poetry config virtualenvs.create false

RUN apt-get update \
    && apt-get install -y \
        postgresql-client \
        # dependencies for psycopg2:
        libpq-dev gcc libc6-dev \
        # dependencies for pdfkit python package:
        wkhtmltopdf \
        --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --only main

COPY rokis_corner           /app/rokis_corner/
COPY apps                   /app/apps/
COPY templates              /app/templates/
COPY static                 /app/static/
COPY manage.py              /app/
COPY scripts/entrypoint     /app/scripts/entrypoint

RUN chmod +x /app/scripts/entrypoint

EXPOSE 8000


FROM base AS prod

CMD ["/app/scripts/entrypoint", "prod"]


FROM base AS local

# Install dev dependencies
RUN poetry install --no-root

CMD ["/app/scripts/entrypoint", "local"]
