FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /tests

# 1) Python-зависимости
COPY tests/requirements.txt /tests/requirements.txt
RUN pip install --no-cache-dir -r /tests/requirements.txt

# 2) Браузеры Playwright + системные зависимости (один раз, в слое образа)
RUN playwright install --with-deps chromium

# 3) Тесты копируются в образ (для CI/прод-подобного запуска);
#    для локальной разработки они монтируются томом (см. compose ниже)
COPY tests/ /tests/

# По умолчанию — прогнать все тесты
CMD ["pytest", "-v"]