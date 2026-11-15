FROM mcr.microsoft.com/playwright/python:v1.64.1-noble

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /tests

COPY docker/e2e/requirements.txt /tests/requirements.txt
RUN pip install --no-cache-dir -r /tests/requirements.txt

RUN playwright install --with-deps chromium

COPY tests/web/e2e/ /tests/

CMD ["pytest", "-v"]