import csv
import json
import os


ARTIFACT_DIR = "artifacts/release"


def ensure_artifact_dir() -> None:
    os.makedirs(ARTIFACT_DIR, exist_ok=True)


def write_json(results: list) -> None:
    ensure_artifact_dir()

    with open(f"{ARTIFACT_DIR}/results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


def write_csv(results: list) -> None:
    ensure_artifact_dir()

    with open(f"{ARTIFACT_DIR}/summary.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["host", "port", "tls_version", "cipher", "risk_score", "risk_level"])

        for result in results:
            writer.writerow([
                result.get("host"),
                result.get("port"),
                result.get("tls_version"),
                result.get("cipher"),
                result.get("risk_score"),
                result.get("risk_level")
            ])


def write_logs(logs: list) -> None:
    ensure_artifact_dir()

    with open(f"{ARTIFACT_DIR}/logs.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(logs))


def write_comparison(comparison: str) -> None:
    ensure_artifact_dir()

    with open(f"{ARTIFACT_DIR}/comparison.txt", "w", encoding="utf-8") as file:
        file.write(comparison)


def write_draft_results() -> None:
    ensure_artifact_dir()

    content = """# Draft Results

Initial testing compares an insecure TLS service against a hardened TLS service.

The insecure service is expected to produce a higher risk score because it may use weaker or deprecated settings.
The secure service is expected to produce a lower risk score because it follows the TLS policy more closely.

This shows that the auditor can distinguish between insecure and improved TLS configurations.
"""

    with open(f"{ARTIFACT_DIR}/draft_results.md", "w", encoding="utf-8") as file:
        file.write(content)