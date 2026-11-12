# =============================================================================
# WEB site commands (no database)
# =============================================================================

WEB_SERVICE_NAME := web
LOG_TAIL     := 200

DC_WEB := docker compose \
	--project-directory . \
	--env-file .envs/web \
	-f compose/networks.yml \
	-f compose/web.base.yml \
	-f compose/web.dev.yml

web-up:  # Build + start web container
	$(DC_WEB) up -d --build

web-stop:  # Stop web container (keeps it around)
	$(DC_WEB) stop $(WEB_SERVICE_NAME)

web-down:  # Down: stop/remove containers and network (no DB volumes in web)
	$(DC_WEB) down

web-restart:  # Restart web process (picks up code from bind-mount; no compose/env/Dockerfile changes)
	$(DC_WEB) restart $(WEB_SERVICE_NAME)

web-recreate:  # Recreate web container: applies compose/env changes (no rebuild)
	$(DC_WEB) up -d --force-recreate --no-deps $(WEB_SERVICE_NAME)

web-rebuild:  # Rebuild + recreate web container: applies Dockerfile/deps changes
	$(DC_WEB) up -d --build --force-recreate --no-deps $(WEB_SERVICE_NAME)

web-logs:  # Follow web logs in real time
	$(DC_WEB) logs -f --tail=$(LOG_TAIL) $(WEB_SERVICE_NAME)

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