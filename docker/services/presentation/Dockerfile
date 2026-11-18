# Presentation Service

# ============ builder ============

FROM python:3.13-slim AS builder

WORKDIR /build

COPY docker/services/presentation/requirements.txt /temp/requirements.txt
RUN pip install \
    --prefix=/install \
    --no-cache-dir \
    --upgrade \
    -r /temp/requirements.txt

# ============ base =============

FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY --from=builder /install /usr/local

COPY ./src/se/application/presentation/ /app/

# ============ dev ============

FROM base

CMD ["fastapi", "run", "app.py", "--port", "8000"]