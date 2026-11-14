# =============================================================================
# E2E tests (Playwright Python)
# =============================================================================

E2E_COMPOSE := docker compose \
	--project-directory . \
	--env-file .envs/db \
	--env-file .envs/db.admin \
	-f compose/networks.yml \
	-f compose/postgres.yml \
	-f compose/db.admin.base.yml \
	-f compose/db.admin.dev.yml \
	-f compose/db.admin.e2e.yml

e2e:  ## Up admin+postgres (keep running) + run e2e (returns pytest exit code)
	@mkdir -p test-results
	$(E2E_COMPOSE) up -d --build admin postgres
	$(E2E_COMPOSE) run --rm --build e2e

e2e-down:  ## Stop admin+postgres+e2e (DB volume kept)
	$(E2E_COMPOSE) down

e2e-build:  ## Rebuild e2e image only (after requirements.txt/Dockerfile changes)
	$(E2E_COMPOSE) build e2e

e2e-logs:  ## Follow e2e logs
	$(E2E_COMPOSE) logs -f --tail=$(LOG_TAIL) e2e

# Help
# ====

e2e-help:
	@echo ""
	@echo "=================================================================="
	@echo "E2E commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "e2e"            "Up admin+postgres + run e2e (admin stays)"
	@printf "$(HELP_FORMAT)" "e2e-down"       "Down all (DB volume kept)"
	@printf "$(HELP_FORMAT)" "e2e-build"      "Rebuild e2e image only"
	@printf "$(HELP_FORMAT)" "e2e-logs"       "Follow e2e logs (tail=$(LOG_TAIL))"
	@echo ""
	@printf "$(HELP_FORMAT)" "e2e-help"       "Show this help"
	@echo ""