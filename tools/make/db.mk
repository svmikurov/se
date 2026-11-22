DB_SERVICE_NAME := se-dev-db-postgres-1

db-conn:
	docker exec -it ${DB_SERVICE_NAME} psql -U se_user -d se