bootstrap:
	pip install -r requirements.txt

up:
	docker compose up --build -d

demo:
	python3 -m src.auditor localhost:8443 localhost:9443
	
test:
	pytest --cov=src --cov-report=term-missing

clean:
	docker compose down -v