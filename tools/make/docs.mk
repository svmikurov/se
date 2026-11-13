# =============================================================================
# Documentation commands
# =============================================================================

-include .envs/docs

DOCS_SERVICE_NAME := se-docs

docs-html:
	poetry run make -C docs/ html

docs-build: ## Build documentation image
	docker build -f docker/docs/Dockerfile -t $(DOCS_SERVICE_NAME) .

docs-run: ## Run documentation server on http://localhost:$(DOCS_HOST_PORT)
	@echo "Running documentation image..."
	-@docker rm -f $(DOCS_SERVICE_NAME)
	docker run --rm -d \
		-p $(DOCS_HOST_PORT):$(DOCS_SERVICE_PORT) \
		-v "$(PWD)/docs/source:/docs/source" \
		--name $(DOCS_SERVICE_NAME) $(DOCS_SERVICE_NAME)
	@echo "🌐 Container started. Docs: http://localhost:$(DOCS_HOST_PORT)"

docs-stop: ## Stop documentation server
	-docker stop $(DOCS_SERVICE_NAME)

# Help
# ====

docs-help:
	@echo ""
	@echo "=================================================================="
	@echo "Documentation commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-html" 		 "Build documentation html"
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-build" "Build documentation image"
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-run"   "Run documentation server on http://localhost:$(DOCS_HOST_PORT)"
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-stop"  "Stop documentation server"
	@echo ""