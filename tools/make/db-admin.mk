# =============================================================================
# Database administration commands
# =============================================================================

include .envs/db
include .envs/http

SERVICE_NAME := admin
DATABASE_NAME := postgres
LOG_TAIL = 200

DC := docker compose \
	--env-file .envs/db \
	--env-file .envs/http \
	-f compose.postgres.yml \
	-f compose.db-admin.yml

admin-up:  # Run database Django administration
	$(DC) up -d --build

admin-stop:  # Stop database Django administration
	$(DC) stop admin

admin-down:  # Stop and remove containers and network (DB volume kept)
	$(DC) down

admin-migrate:  # Apply Django migrations (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py migrate

admin-migrate-plan:  # Show migration plan without applying (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py migrate --plan

admin-makemigrations:  # Generate new migrations from model changes (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py makemigrations

admin-logs:  # Follow application logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(SERVICE_NAME)

admin-logs-db:  # Follow Postgres logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(DATABASE_NAME)

admin-dumpdata:
	@test -n "$(DUMP_MODELS)" || { echo "ERROR: DUMP_MODELS is empty"; exit 1; }
	@mkdir -p dumps
	$(DC) exec -T $(SERVICE_NAME) python manage.py dumpdata $(DUMP_MODELS) --indent 2 > dumps/dump-$(shell date +%Y%m%d-%H%M%S).json
	@echo "dump written to dumps/"

# Help
# ====

admin-help:
	@echo ""
	@echo "=================================================================="
	@echo "Database administration commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-run"	"Run database Django administration"
	@echo ""