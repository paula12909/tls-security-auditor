# Runbook

## Prerequisites

-   Docker Desktop installed and running
-   Git installed
-   A terminal available

## Clone the Repository

git clone https://github.com/paula12909/tls-security-auditor.git cd
tls-security-auditor

## Run the Full System

make up && make demo

## Expected Output

localhost:8443 -\> HIGH risk localhost:9443 -\> LOW risk

\[INFO\] Artifacts written to artifacts/release/

## View Artifacts

ls artifacts/release

## Stop the System

make down

## Rebuild

make down make up make demo

## Run Tests

python3 -m venv venv source venv/bin/activate pip install pytest
pytest-cov pytest --cov=src

## Troubleshooting

If Docker is not running, open Docker Desktop.

If pytest is missing, install it in a virtual environment.

## Clean Up

make down
