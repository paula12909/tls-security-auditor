def score_issues(issues: list) -> tuple:
    score = 0

    for issue in issues:
        text = issue.lower()

        if "deprecated tls" in text:
            score += 4
        elif "weak cipher" in text:
            score += 3
        elif "no certificate" in text:
            score += 3
        elif "self-signed" in text:
            score += 2
        elif "connection error" in text:
            score += 4
        elif "demo insecure" in text:
            score += 6
        else:
            score += 1

    if score >= 6:
        risk_level = "HIGH"
    elif score >= 3:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return score, risk_level