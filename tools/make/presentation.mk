# =============================================================================
# Presentation service commands
# =============================================================================

PRESENTATION_SERVICE_NAME := presentation
PRESENTATION_HOST_PORT := 8400
PRESENTATION_SERVICE_PORT := 8000

DC_PRESENTATION := docker compose \
	--project-directory . \
	--env-file .envs/presentation \
	-f compose/networks.yml \
	-f compose/app.presentation.yml

presentation-build: ## Build service image
	docker build -f docker/services/presentation/Dockerfile -t $(PRESENTATION_SERVICE_NAME) .

presentation-run:  ## Run service server on http://localhost:$(PRESENTATION_SERVICE_NAME)
	@echo "Running Presentation service image..."
	-@docker rm -f $(PRESENTATION_SERVICE_NAME)
	docker run --rm \
		-p $(PRESENTATION_HOST_PORT):$(PRESENTATION_SERVICE_PORT) \
		--name $(PRESENTATION_SERVICE_NAME) $(PRESENTATION_SERVICE_NAME) 
	@echo "🌐 Container started. Service: http://localhost:$(PRESENTATION_HOST_PORT)"

presentation-stop: ## Stop service server
	-docker stop $(PRESENTATION_SERVICE_NAME)

presentation-logs:
	docker logs $(PRESENTATION_SERVICE_NAME)

presentation-up:  ## Build + start container
	$(DC_PRESENTATION) up -d --build

presentation-down:  ## Down: stop/remove container
	$(DC_PRESENTATION) down	

presentation-restart:  ## Restart service process (picks up code from bind-mount; no compose/env/Dockerfile changes)
	$(DC_PRESENTATION) restart $(PRESENTATION_SERVICE_NAME)

presentation-recreate:  ## Recreate service container: applies compose/env changes (no rebuild)
	$(DC_PRESENTATION) up -d --force-recreate --no-deps $(PRESENTATION_SERVICE_NAME)

wpresentationeb-rebuild:  ## Rebuild + recreate service container: applies Dockerfile/deps changes
	$(DC_PRESENTATION) up -d --build --force-recreate --no-deps $(PRESENTATION_SERVICE_NAME)

# Help
# ====

presentation-help:
	@echo ""
	@echo "=================================================================="
	@echo "Presentation service commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-build" "Build service image"
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-run"   "Run service server on http://localhost:$(PRESENTATION_HOST_PORT)"
	@printf "$(HELP_FORMAT)" "presentation-stop"  "Stop service server"
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-up"	  "Build + start container"
	@printf "$(HELP_FORMAT)" "presentation-down"  "Down: stop/remove container"
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-restart"		"Restart service process (bind-mount code only)"
	@printf "$(HELP_FORMAT)" "presentation-recreate"	"Recreate service container (compose/env changes, no rebuild)"
	@printf "$(HELP_FORMAT)" "presentation-rebuild"		"Rebuild + recreate service container (Dockerfile/deps changes)"
	@echo ""