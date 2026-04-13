# TLS Security Auditor

## Overview
This project builds a reproducible TLS Security Auditor that scans local services and detects insecure TLS configurations such as:
- Deprecated TLS versions
- Weak cipher suites
- Expired or self-signed certificates

## Features
- Automated TLS configuration scanning
- Risk scoring and severity classification
- Before/after comparison (insecure vs secure services)
- Docker-based reproducible environment

## Setup

### One-command bootstrap
```bash
make bootstrap
