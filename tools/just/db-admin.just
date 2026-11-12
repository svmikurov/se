# =============================================================================
# Database administration commands
# =============================================================================

ROOT := "../../"
ADMIN_SERVICE_NAME := "admin"
DUMPS_PATH := "/app/dumps/"

ADMIN_DC := "docker compose" + \
    " --env-file " + ROOT + ".envs/db" + \
    " --env-file " + ROOT + ".envs/db.admin" + \
    " -f " + ROOT + "compose.postgres.yml" + \
    " -f " + ROOT + "compose.db-admin.base.yml" + \
    " -f " + ROOT + "compose.db-admin.dev.yml"

# Load dumps to database from ./dumps/{file}.json
ld file:
    MSYS_NO_PATHCONV=1 {{ADMIN_DC}} exec -T {{ADMIN_SERVICE_NAME}} python manage.py loaddata {{DUMPS_PATH}}{{file}}.json