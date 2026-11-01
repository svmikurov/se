# =============================================================================
# Project commands
# =============================================================================

include .envs/db.secrets

environments:  # Generate environment examples: ./envs/* from .envs.example/*
	cp -r .envs.example/ .envs/

.PHONY: secrets
secrets:  # Generate secret examples: ./secrets/* from .envs/*.secrets
	@mkdir -p secrets
	@umask 077 && printf '%s\n' "$(DATABASE_PASSWORD)" > secrets/database_password
	@chmod 600 secrets/database_password

.PHONY: setup
setup: ## Install project with dependencies
	poetry install

clean: ## Remove cache files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true

# Help
# ====

app-help:
	@echo ""
	@echo "=================================================================="
	@echo "Project commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "environments"	"Generate environment examples: ./envs/* from .envs.example/*"
	@echo ""
	@printf "$(HELP_FORMAT)" "secrets"		"Generate secret examples: ./secrets/* from .envs/*.secrets"
	@echo ""
	@printf "$(HELP_FORMAT)" "setup"		"Install project with dependencies"
	@echo ""
	@printf "$(HELP_FORMAT)" "clean"		"Remove cache files"
	@echo ""