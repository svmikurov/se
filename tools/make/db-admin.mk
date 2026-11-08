# =============================================================================
# Database administration commands
# =============================================================================

SERVICE_NAME := admin
DATABASE_NAME := postgres
LOG_TAIL := 200
DUMP_MODELS := auth.user glossary

DC := docker compose \
	--env-file .envs/db \
	--env-file .envs/db.admin \
	-f compose.postgres.yml \
	-f compose.db-admin.base.yml \
	-f compose.db-admin.dev.yml

admin-up:  # Run database Django administration
	$(DC) up -d --build

admin-stop:  # Stop database Django administration
	$(DC) stop $(SERVICE_NAME)

admin-down:  # Stop and remove containers and network (DB volume kept)
	$(DC) down

admin-down-hard:  # DANGER: down + drop named volume postgres-data
	$(DC) down --volumes

admin-migrate:  # Apply Django migrations (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py migrate

admin-migrate-plan:  # Show migration plan without applying (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py migrate --plan

admin-makemigrations:  # Generate new migrations from model changes (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py makemigrations

admin-su:  # Create super user
	$(DC) exec $(SERVICE_NAME) python manage.py createsuperuser

admin-logs:  # Follow application logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(SERVICE_NAME)

admin-logs-db:  # Follow Postgres logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(DATABASE_NAME)

admin-dumpdata:  # Dump models to dumps/dump-<timestamp>.json (DUMP_MODELS=$(DUMP_MODELS))
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
	@printf "$(HELP_FORMAT)" "admin-up"              "Run database Django administration (build + up -d)"
	@printf "$(HELP_FORMAT)" "admin-stop"            "Stop admin container (keeps it around)"
	@printf "$(HELP_FORMAT)" "admin-down"            "Stop and remove containers and network (DB volume kept)"
	@printf "$(HELP_FORMAT)" "admin-down-hard"       "DANGER: down + drop named volume postgres-data"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-migrate"         "Apply Django migrations (dev)"
	@printf "$(HELP_FORMAT)" "admin-migrate-plan"    "Show migration plan without applying (dev)"
	@printf "$(HELP_FORMAT)" "admin-makemigrations"  "Generate new migrations from model changes (dev)"
	@printf "$(HELP_FORMAT)" "admin-su"              "Create Django superuser"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-logs"            "Follow application logs in real time (tail=$(LOG_TAIL))"
	@printf "$(HELP_FORMAT)" "admin-logs-db"         "Follow Postgres logs in real time (tail=$(LOG_TAIL))"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-dumpdata"        "Dump models to dumps/dump-<timestamp>.json (DUMP_MODELS=$(DUMP_MODELS))"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-help"            "Show this help"
	@echo ""