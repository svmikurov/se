# =============================================================================
# Network commands
# =============================================================================

EXTERNAL_NETWORK := se-dev-net

net-create:  # Create external network
	docker network create $(EXTERNAL_NETWORK)

net-ls:  # Show networks
	docker network ls

net-rm:  # Remove network
	docker network rm $(EXTERNAL_NETWORK)

# -----------------------------------------------------------------------------
# Help
# -----------------------------------------------------------------------------

net-help:
	@echo ""
	@echo "=================================================================="
	@echo "External networks commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "net-create"      "Create external networks"
	@printf "$(HELP_FORMAT)" "net-ls"          "Show networks"
	@printf "$(HELP_FORMAT)" "net-rm"          "Remove networks"
	@echo ""
	@printf "$(HELP_FORMAT)" "net-help"        "Show this help"
	@echo ""