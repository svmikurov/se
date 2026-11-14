# =============================================================================
# WEB site E2E tests (Playwright Python)
# =============================================================================

E2E_WEB_COMPOSE := docker compose \
	--project-directory . \
	--env-file .envs/web \
	-f compose/networks.yml \
	-f compose/web.e2e.yml

web-e2e:  # Run Playwright E2E against web (web must be running)
	@mkdir -p test-results
	$(E2E_WEB_COMPOSE) run --rm --build web-e2e

web-e2e-logs:  # Follow web-e2e container logs
	$(E2E_WEB_COMPOSE) logs -f --tail=$(LOG_TAIL) web-e2e

# Help
# ====

web-e2e-help:
	@echo ""
	@echo "=================================================================="
	@echo "WEB site E2E commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "web-e2e"         "Run Playwright E2E against web (web must be running)"
	@printf "$(HELP_FORMAT)" "web-e2e-logs"    "Follow web-e2e container logs (tail=$(LOG_TAIL))"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-e2e-help"    "Show this help"
	@echo ""