# Presentation Service

# ============ base-builder ============

FROM python:3.13-slim AS base-builder

WORKDIR /build

# Some project dependencies installed from GitHub repositories
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    git \
 && rm -rf /var/lib/apt/lists/*


# ============ base-builder ============

FROM base-builder AS builder

WORKDIR /build

ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/ \
    PIP_TRUSTED_HOST=mirrors.aliyun.com \
    PIP_DEFAULT_TIMEOUT=100

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

COPY ./src/se/domain/                       /app/se/domain/
COPY ./src/se/application/                  /app/se/application/
COPY ./src/se/infrastructure/repositories   /app/se/infrastructure/repositories


# ============ dev ============

FROM base

CMD ["fastapi", "run", "se/application/presentation/main.py", "--port", "8000"]