E2E_COMPOSE := docker compose \
	--env-file .envs/db \
	--env-file .envs/db.admin \
	-f compose/postgres.yml \
	-f compose/db.admin.base.yml \
	-f compose/db.admin.dev.yml \
	-f compose/db.admin.e2e.yml

e2e:  # Run Playwright Python E2E tests (image with baked-in Playwright)
	@mkdir -p test-results
	$(E2E_COMPOSE) up \
		--build \
		--abort-on-container-exit \
		--exit-code-from e2e

e2e-down:
	$(E2E_COMPOSE) down

e2e-build:  # Пересобрать e2e-образ (после изменения requirements.txt/Dockerfile)
	$(E2E_COMPOSE) build e2e