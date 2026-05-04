# Contribution Log and Code Ownership Map

## Contribution Log

Al Jayson Mendoza was responsible for the core system functionality of the TLS Security Auditor. His work included implementing the TLS scanning and connection logic, developing the security checks used to detect misconfigurations, and setting up the Docker-based test environment. This environment includes both secure and insecure services, allowing the system to be tested in a controlled and reproducible setting.

Paula Awad was responsible for the evaluation and analysis components of the system. Her work included implementing the risk scoring logic, developing the reporting system that generates JSON, CSV, and log outputs, and building the comparison functionality used to evaluate multiple targets. She also created the test suite, configured the CI pipeline, and generated the evaluation artifacts and analysis used in the project.

Both team members collaborated on integrating all components into the main pipeline through the auditor module. They also worked together on documentation, including the README, RUNBOOK, and supporting project files, as well as preparing the demo and validating that the system runs correctly end-to-end.

## Code Ownership Map

| Component | Owner |
|----------|------|
| src/scanner.py | Al Jayson Mendoza |
| src/checks.py | Al Jayson Mendoza |
| test_services/ | Al Jayson Mendoza |
| docker-compose.yml | Al Jayson Mendoza |
| src/scoring.py | Paula Awad |
| src/report.py | Paula Awad |
| src/compare.py | Paula Awad |
| tests/ | Paula Awad |
| .github/workflows/ci.yml | Paula Awad |
| artifacts/release/ | Paula Awad |
| src/auditor.py | Shared |
| README.md | Shared |
| RUNBOOK.md | Shared |
| SECURITY_INVARIANTS.md | Shared |
| WHAT_WORKS_WHATS_NEXT.md | Shared |
| docs/demo.mov | Shared |
