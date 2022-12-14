FROM python:3.10-slim AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN pip install poetry; \
    python -m venv .venv; \
    . .venv/bin/activate; \
    poetry install --without dev; \
    deactivate;


FROM python:3.10-slim as runner
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY . /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app;$/app/.venv/lib/python3.10/site-packages"
ENV TOKEN=""
ENV GUILD_IDS=""
ENTRYPOINT [ "python", "-m", "spacebot" ]
