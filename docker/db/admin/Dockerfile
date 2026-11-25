# Database management via Django framework.

# ============ base-builder ============

FROM python:3.13-slim AS base-builder

WORKDIR /build

# Some project dependencies installed from GitHub repositories
RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*


# ============ builder ============

FROM base-builder AS builder

WORKDIR /build

ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/ \
    PIP_TRUSTED_HOST=mirrors.aliyun.com \
    PIP_DEFAULT_TIMEOUT=100

COPY docker/db/admin/requirements.txt /temp/requirements.txt
RUN pip3 install \
    --prefix=/install \
    --no-cache-dir \
    -r /temp/requirements.txt


# ============ base ============

FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY --from=builder /install /usr/local


# ============ dev ============

FROM base AS dev


# ============ prod ============

FROM base AS prod

COPY src/se/infrastructure/db/admin /app

RUN useradd -r -u 10001 -g nogroup appuser \
 && chown -R appuser:nogroup /app

USER 10001:10001

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", "--workers", "3", \
     "--access-logfile", "-", "--error-logfile", "-"]