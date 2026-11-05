# =============================================================================
# Just commands
# =============================================================================

DC := "docker compose \
    --env-file .envs/db \
    --env-file .envs/db.admin \
    -f compose.postgres.yml \
    -f compose.db-admin.yml    "
SERVICE_NAME := "admin"


# Database administration commands
# ================================

DUMPS_PATH := "/app/dumps/"

ld file:  # Load data to database
    MSYS_NO_PATHCONV=1 {{DC}} exec -T {{SERVICE_NAME}} python manage.py loaddata {{DUMPS_PATH}}{{file}}.json