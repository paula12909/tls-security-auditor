import json
import sys

from src.scanner import scan_target
from src.checks import run_checks
from src.scoring import score_issues
from src.compare import compare_results
from src.report import write_json, write_csv, write_logs, write_comparison, write_draft_results

def load_policy(path: str = "policy/tls_policy.json") -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def parse_target(target: str) -> tuple:
    if ":" not in target:
        raise ValueError("Target must be in host:port format")

    host, port_text = target.split(":", 1)
    port = int(port_text)

    return host, port


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python src/auditor.py host:port [host:port ...]")
        sys.exit(1)

    policy = load_policy()
    results = []
    logs = []

    for target in sys.argv[1:]:
        try:
            host, port = parse_target(target)

            print(f"\n[INFO] Scanning {host}:{port}")
            logs.append(f"[INFO] Scanning {host}:{port}")

            result = scan_target(host, port)
            issues = run_checks(result, policy)
            score, risk_level = score_issues(issues)

            result["issues"] = issues
            result["risk_score"] = score
            result["risk_level"] = risk_level

            results.append(result)

            logs.append(f"[INFO] Connected: {result.get('connected')}")
            logs.append(f"[INFO] TLS Version: {result.get('tls_version')}")
            logs.append(f"[INFO] Cipher: {result.get('cipher')}")
            logs.append(f"[INFO] Risk: {risk_level} ({score})")

            print(f"TLS Version: {result.get('tls_version')}")
            print(f"Cipher: {result.get('cipher')}")
            print(f"Risk Level: {risk_level}")
            print(f"Risk Score: {score}")

            if issues:
                print("Findings:")
                for issue in issues:
                    print(f"- {issue}")
                    logs.append(f"[FINDING] {issue}")
            else:
                print("Findings: No issues detected")
                logs.append("[FINDING] No issues detected")

        except Exception as error:
            print(f"[ERROR] Failed to scan {target}: {error}")
            logs.append(f"[ERROR] Failed to scan {target}: {error}")

    comparison = compare_results(results)

    print("\n--- Comparison ---")
    print(comparison)

    write_json(results)
    write_csv(results)
    write_logs(logs)
    write_comparison(comparison)
    write_draft_results()

    print("\n[INFO] Artifacts written to artifacts/release/")


if __name__ == "__main__":
    main()