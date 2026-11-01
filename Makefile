# =============================================================================
# Makefile commands
# =============================================================================

include tools/make/app.mk
include tools/make/check.mk
include tools/make/db-admin.mk

COLUMN_WIDTH := 24
HELP_FORMAT := %-$(COLUMN_WIDTH)s %s\n

# Help
# ====

help:
	@echo "=================================================================="
	@echo "Makefile commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "app-help"				"Project commands help"
	@printf "$(HELP_FORMAT)" "check-help"			"Code quality commands help"
	@printf "$(HELP_FORMAT)" "admin-help"			"Add environments example"
	@echo ""

help-all:
	@$(MAKE) --no-print-directory app-help
	@$(MAKE) --no-print-directory check-help
	@$(MAKE) --no-print-directory admin-help