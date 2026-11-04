# Database management via Django framework.

FROM python:3.13-slim AS builder

WORKDIR /build

# Some project dependencies installed from GitHub repositories
RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*

COPY docker/db/admin/requirements.txt /temp/requirements.txt
RUN pip3 install \
    --prefix=/install \
    --no-cache-dir \
    -r /temp/requirements.txt


FROM python:3.13-slim AS dev

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app
    
WORKDIR /app

COPY --from=builder /install /usr/local

COPY src/se/infra/db/admin /app