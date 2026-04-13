bootstrap:
	docker compose build
	docker compose up -d
	@echo "Environment ready. Run 'docker compose logs auditor' to see results."
