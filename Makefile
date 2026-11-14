# =============================================================================
# Makefile commands
# =============================================================================

include tools/make/app.mk
include tools/make/docs.mk
include tools/make/check.mk
include tools/make/e2e.mk
include tools/make/db.admin.mk
include tools/make/net.mk
include tools/make/web.mk

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
	@printf "$(HELP_FORMAT)" "e2e-help"		"E2E tests (Playwright Python) commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "admin-help"	"Database administration commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "net-help"		"Network commands help"
	@echo ""
	@printf "$(HELP_FORMAT)" "web-help"		"WEB site commands (no database) help"
	@echo ""
	@printf "$(HELP_FORMAT)" "help-all"		"Database administration commands help"
	@echo ""

help-all:
	@$(MAKE) --no-print-directory app-help
	@$(MAKE) --no-print-directory docs-help
	@$(MAKE) --no-print-directory check-help
	@$(MAKE) --no-print-directory e2e-help
	@$(MAKE) --no-print-directory admin-help
	@$(MAKE) --no-print-directory net-help
	@$(MAKE) --no-print-directory web-help