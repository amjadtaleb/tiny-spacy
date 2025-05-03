# ---- Builder stage ----
FROM python:3.11-slim AS builder

RUN pip install --upgrade pip && pip install uv

WORKDIR /venv
RUN uv init
RUN uv add spacy pip "fastapi[standard]"
RUN uv run --with spacy -- spacy download en_core_web_md

# ---- Runner stage ----
FROM python:3.11-slim AS runner

COPY --from=builder /venv /venv
ENV PATH="/venv/.venv/bin:$PATH"

WORKDIR /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
