# Security Invariants

## 1. No plaintext secrets are written to disk
The auditor does not store private keys, passwords, or sensitive plaintext data in output artifacts.

## 2. TLS findings are logged, not sensitive payloads
Logs only record scan results such as TLS version, cipher, certificate status, risk score, and detected issues.

## 3. Inputs are limited to target host and port
The system only scans the targets provided to the auditor and does not perform unrelated network activity.

## 4. Insecure TLS configurations are flagged
Deprecated TLS versions, missing certificates, weak cipher information, or failed TLS handshakes are reported as security findings.

## 5. Artifacts are reproducible
Generated evidence is written to `artifacts/release/` so results can be reviewed and verified.

## 6. Docker services are isolated
Secure and insecure demo services run inside Docker containers to keep testing separated from the host system.

## 7. Failures are handled safely
Connection errors and invalid targets are reported as findings instead of crashing silently or hiding risk.
