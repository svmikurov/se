# =============================================================================
# Presentation service commands
# =============================================================================

PRESENTATION_SERVICE_NAME := presentation
PRESENTATION_HOST_PORT := 8400
PRESENTATION_SERVICE_PORT := 8000

DC_PRESENTATION := docker compose \
	--project-directory . \
	--env-file .envs/presentation \
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
	-docker stop $(DOCS_SERVICE_NAME)

presentation-logs:
	docker logs $(PRESENTATION_SERVICE_NAME)

presentation-up:  ## Build + start container
	$(DC_PRESENTATION) up -d --build

presentation-down:  ## Down: stop/remove container
	$(DC_PRESENTATION) down	

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
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-stop"  "Stop service server"
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-up"	  "Build + start container"
	@echo ""
	@printf "$(HELP_FORMAT)" "presentation-down"  "Down: stop/remove container"
	@echo ""