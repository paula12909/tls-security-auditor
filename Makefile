# bootstrap:
# 	docker compose build
# 	docker compose up -d
# 	@echo "Environment ready. Run 'docker compose logs auditor' to see results."

bootstrap:
	pip install -r requirements.txt

up:
	docker-compose up --build -d

demo:
	python src/auditor.py localhost:8443 localhost:9443

test:
	pytest --cov=src --cov-report=term-missing

down:
	docker-compose down

clean:
	rm -f artifacts/release/results.json artifacts/release/summary.csv artifacts/release/logs.txt artifacts/release/comparison.txt