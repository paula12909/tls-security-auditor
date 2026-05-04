#Team Members:
Paula Awad
Al Jayson Mendoza

## Quick Start

Run the full system (required):

```bash
make up && make demo

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

## Run the System
make up
make demo

##Artifacts
After running the demo, results are stored in:
artifacts/release/
Includes:
logs.txt
summary.csv
summary.json
comparison.txt
draft_results.md

## Architecture

The TLS Security Auditor is composed of several modular components that work together to analyze TLS configurations.

### Components

- **Scanner (`scanner.py`)**
  Connects to target services and retrieves TLS information such as version, cipher suite, and certificate details.

- **Checks (`checks.py`)**
  Applies validation rules to detect insecure configurations such as missing certificates or deprecated protocols.

- **Scoring (`scoring.py`)**
  Assigns a numerical risk score based on detected issues.

- **Compare (`compare.py`)**
  Compares multiple targets and determines which configuration is more secure.

- **Report (`report.py`)**
  Generates output artifacts including logs, JSON summaries, CSV metrics, and comparison results.

- **Auditor (`auditor.py`)**
  Orchestrates the entire workflow: scanning → checking → scoring → reporting.

### System Flow

1. Docker launches secure and insecure TLS services
2. Auditor scans each service
3. TLS data is collected and analyzed
4. Risk scores are computed
5. Results are compared
6. Artifacts are written to `artifacts/release/`

This modular design allows each component to be tested independently while supporting a complete end-to-end system.
