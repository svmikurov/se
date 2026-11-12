# =============================================================================
# Database administration commands
# =============================================================================

SERVICE_NAME   := admin
DATABASE_SERVICE := postgres
LOG_TAIL       := 200
DUMP_MODELS    := auth.user glossary

DC := docker compose \
	--env-file .envs/db \
	--env-file .envs/db.admin \
	-f compose/postgres.yml \
	-f compose/db.admin.base.yml \
	-f compose/db.admin.dev.yml

admin-up:  # Build + start admin and postgres (DB volume kept)
	@mkdir -p dumps
	$(DC) up -d --build

admin-stop:  # Stop admin container (keeps it around)
	$(DC) stop $(SERVICE_NAME)

admin-down:  # Down: stop/remove containers and network; named DB volume KEPT
	$(DC) down

admin-down-hard:  # DANGER: down + drop named DB volume (data LOST)
	$(DC) down --volumes

admin-restart:  # Restart admin process (picks up code from bind-mount; no compose/env/Dockerfile changes)
	$(DC) restart $(SERVICE_NAME)

admin-recreate:  # Recreate admin container: applies compose/env changes (no rebuild)
	$(DC) up -d --force-recreate --no-deps $(SERVICE_NAME)

admin-rebuild:  # Rebuild + recreate admin: applies Dockerfile/deps changes
	$(DC) up -d --build --force-recreate --no-deps $(SERVICE_NAME)

admin-makemigrations:  # Generate new migrations from model changes (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py makemigrations

admin-dry-run:  # Preview model changes -> migrations, without writing files
	$(DC) exec $(SERVICE_NAME) python manage.py makemigrations --dry-run

admin-migrate:  # Apply Django migrations to the DB (dev)
	$(DC) exec $(SERVICE_NAME) python manage.py migrate

admin-migrate-plan:  # Show which migrations would be applied, without applying
	$(DC) exec $(SERVICE_NAME) python manage.py migrate --plan

admin-showmigrations:  # List all migrations and their applied/unapplied state
	$(DC) exec $(SERVICE_NAME) python manage.py showmigrations

admin-su:  # Create Django superuser (interactive)
	$(DC) exec $(SERVICE_NAME) python manage.py createsuperuser

admin-logs:  # Follow admin logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(SERVICE_NAME)

admin-logs-db:  # Follow Postgres logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(DATABASE_SERVICE)

admin-dumpdata:  # Dump DUMP_MODELS to dumps/dump-<timestamp>.json
	@test -n "$(DUMP_MODELS)" || { echo "ERROR: DUMP_MODELS is empty"; exit 1; }
	@mkdir -p dumps
	@tmp=$$(mktemp dumps/.dump-XXXXXX.json); \
	if $(DC) exec -T $(SERVICE_NAME) python manage.py dumpdata $(DUMP_MODELS) --indent 2 > $$tmp; then \
		mv $$tmp dumps/dump-$$(date +%Y%m%d-%H%M%S).json; \
		echo "dump written to dumps/"; \
	else \
		rc=$$?; rm -f $$tmp; echo "ERROR: dumpdata failed (rc=$$rc)"; exit $$rc; \
	fi

# Help
# ====

admin-help:
	@echo ""
	@echo "=================================================================="
	@echo "Database administration commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-up"              "Build + start admin and postgres (DB volume kept)"
	@printf "$(HELP_FORMAT)" "admin-stop"            "Stop admin container (keeps it around)"
	@printf "$(HELP_FORMAT)" "admin-down"            "Down; named DB volume KEPT"
	@printf "$(HELP_FORMAT)" "admin-down-hard"       "DANGER: down + drop DB volume (data LOST)"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-restart"         "Restart admin process (bind-mount code only)"
	@printf "$(HELP_FORMAT)" "admin-recreate"        "Recreate admin (compose/env changes, no rebuild)"
	@printf "$(HELP_FORMAT)" "admin-rebuild"         "Rebuild + recreate admin (Dockerfile/deps changes)"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-makemigrations"  "Generate migrations from model changes"
	@printf "$(HELP_FORMAT)" "admin-dry-run"         "Preview migrations without writing files"
	@printf "$(HELP_FORMAT)" "admin-migrate"         "Apply migrations to the DB"
	@printf "$(HELP_FORMAT)" "admin-migrate-plan"    "Show migration plan without applying"
	@printf "$(HELP_FORMAT)" "admin-showmigrations"  "List migrations and applied state"
	@printf "$(HELP_FORMAT)" "admin-su"              "Create Django superuser"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-logs"            "Follow admin logs (tail=$(LOG_TAIL))"
	@printf "$(HELP_FORMAT)" "admin-logs-db"         "Follow Postgres logs (tail=$(LOG_TAIL))"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-dumpdata"        "Dump $(DUMP_MODELS) to dumps/dump-<timestamp>.json"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-help"            "Show this help"
	@echo ""