FROM python:3.10-slim AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN pip install poetry; \
    python -m venv .venv; \
    . .venv/bin/activate; \
    poetry install --no-dev; \
    deactivate;


FROM python:3.10-slim as runner
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY ./spacebot /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app;$/app/.venv/lib/python3.10/site-packages"
ENTRYPOINT [ "python", "-m", "spacebot" ]
