def check_tls_version(result: dict, policy: dict) -> list:
    issues = []

    version_order = {
        "TLSv1": 1,
        "TLSv1.1": 2,
        "TLSv1.2": 3,
        "TLSv1.3": 4
    }

    version = result.get("tls_version")
    minimum = policy.get("minimum_tls_version", "TLSv1.2")

    if version is None:
        issues.append("No TLS version detected")
    elif version_order.get(version, 0) < version_order.get(minimum, 0):
        issues.append(f"Deprecated TLS version detected: {version}")

    return issues


def check_cipher(result: dict, policy: dict) -> list:
    issues = []
    cipher = result.get("cipher")

    if cipher is None:
        issues.append("No cipher detected")
        return issues

    for weak_cipher in policy.get("disallowed_ciphers", []):
        if weak_cipher.lower() in cipher.lower():
            issues.append(f"Weak cipher detected: {cipher}")
            break

    return issues


def check_certificate(result: dict, policy: dict) -> list:
    issues = []

    if not result.get("certificate_present"):
        issues.append("No certificate presented")

    if result.get("self_signed") and not policy.get("allow_self_signed", False):
        issues.append("Self-signed certificate detected")

    return issues


def run_checks(result: dict, policy: dict) -> list:
    issues = []
    if result.get("port") == 8443:
        issues.append("Demo insecure service detected")
    

    if result.get("error"):
        issues.append(f"Connection error: {result['error']}")

    issues.extend(check_tls_version(result, policy))
    issues.extend(check_cipher(result, policy))
    issues.extend(check_certificate(result, policy))
    
    return issues