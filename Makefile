# =============================================================================
# Makefile commands
# =============================================================================

include tools/make/app.mk
include tools/make/docs.mk
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
	@printf "$(HELP_FORMAT)" "app-help"		"Project commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-help"	"Project documentation commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "check-help"	"Code quality commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-help"	"Database administration commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "help-all"		"Database administration commands help"
	@echo ""

help-all:
	@$(MAKE) --no-print-directory app-help
	@$(MAKE) --no-print-directory docs-help
	@$(MAKE) --no-print-directory check-help
	@$(MAKE) --no-print-directory admin-help