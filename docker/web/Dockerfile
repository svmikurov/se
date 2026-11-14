# Django framework WEB entrypoint.

# ============ builder ============

FROM python:3.13-slim AS builder

WORKDIR /build

# Some project dependencies installed from GitHub repositories
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    git \
 && rm -rf /var/lib/apt/lists/*

COPY docker/web/requirements.txt /temp/requirements.txt
RUN pip3 install \
    --prefix=/install \
    --no-cache-dir \
    -r /temp/requirements.txt

# ============ base ============

FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gettext \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /install /usr/local

# ============ dev ============

FROM base AS dev
