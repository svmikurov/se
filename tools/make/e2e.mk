# =============================================================================
# WEB site E2E tests (Playwright Python)
# =============================================================================

# IDEA:

E2E_SERVICE_NAME := test
LOG_TAIL		 := 50

DC_e2e = docker compose \
	--project-directory . \
	--env-file .envs/db \
	--env-file .envs/db.admin \
	--env-file .envs/presentation \
	--env-file .envs/web \
	-f compose/e2e.yml

e2e-up:
	$(DC_e2e) run --rm --build $(E2E_SERVICE_NAME)

e2e-logs:
	$(DC_e2e) logs -f --tail=$(LOG_TAIL) $(E2E_SERVICE_NAME)
