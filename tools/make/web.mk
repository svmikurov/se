# =============================================================================
# WEB site commands (no database)
# =============================================================================

SERVICE_NAME := web
LOG_TAIL     := 200

DC := docker compose \
	--env-file .envs/web \
	-f compose/web.base.yml \
	-f compose/web.dev.yml

web-up:  # Build + start web container
	$(DC) up -d --build

web-stop:  # Stop web container (keeps it around)
	$(DC) stop $(SERVICE_NAME)

web-down:  # Down: stop/remove containers and network (no DB volumes in web)
	$(DC) down

web-restart:  # Restart web process (picks up code from bind-mount; no compose/env/Dockerfile changes)
	$(DC) restart $(SERVICE_NAME)

web-recreate:  # Recreate web container: applies compose/env changes (no rebuild)
	$(DC) up -d --force-recreate --no-deps $(SERVICE_NAME)

web-rebuild:  # Rebuild + recreate web container: applies Dockerfile/deps changes
	$(DC) up -d --build --force-recreate --no-deps $(SERVICE_NAME)

web-logs:  # Follow web logs in real time
	$(DC) logs -f --tail=$(LOG_TAIL) $(SERVICE_NAME)

# Help
# ====

web-help:
	@echo ""
	@echo "=================================================================="
	@echo "WEB site commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "web-up"         "Build + start web container"
	@printf "$(HELP_FORMAT)" "web-stop"       "Stop web container (keeps it around)"
	@printf "$(HELP_FORMAT)" "web-down"       "Down: stop/remove containers and network"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-restart"    "Restart web process (bind-mount code only)"
	@printf "$(HELP_FORMAT)" "web-recreate"   "Recreate web container (compose/env changes, no rebuild)"
	@printf "$(HELP_FORMAT)" "web-rebuild"    "Rebuild + recreate web container (Dockerfile/deps changes)"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-logs"       "Follow web logs (tail=$(LOG_TAIL))"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-help"       "Show this help"
	@echo ""