# Database management via Django framework.

FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*

COPY docker/db/admin/requirements.txt /temp/requirements.txt
RUN pip3 install -r /temp/requirements.txt --no-cache-dir

COPY src/se/infra/db/admin  /app