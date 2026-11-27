# =============================================================================
# Makefile commands
# =============================================================================

include .envs/db.admin

include tools/make/docs.mk
include tools/make/app.mk
include tools/make/check.mk
include tools/make/net.mk
include tools/make/db.mk
include tools/make/db.admin.mk
include tools/make/web.mk
include tools/make/web.e2e.mk
include tools/make/e2e.mk
include tools/make/presentation.mk

COLUMN_WIDTH := 24
HELP_FORMAT  := %-$(COLUMN_WIDTH)s %s\n

# Help
# ====

help:
	@echo "=================================================================="
	@echo "Makefile commands help"
	@echo "=================================================================="
	@echo ""
	@printf "$(HELP_FORMAT)" "docs-help"	"Project documentation commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "app-help"		"Project commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "check-help"	"Code quality commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "net-help"		"Network commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-help"	"Database administration commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-help"		"WEB site commands (no database) help"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-e2e-help"	"WEB site E2E tests (Playwright Python) commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "help-all"		"All help commands"
	@echo ""

help-all:
	@$(MAKE) --no-print-directory docs-help
	@$(MAKE) --no-print-directory app-help
	@$(MAKE) --no-print-directory check-help
	@$(MAKE) --no-print-directory net-help
	@$(MAKE) --no-print-directory admin-help
	@$(MAKE) --no-print-directory web-help
	@$(MAKE) --no-print-directory web-e2e-help