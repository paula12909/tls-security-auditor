from src.scoring import score_issues


def test_no_issues_is_low_risk():
    score, risk = score_issues([])
    assert score == 0
    assert risk == "LOW"


def test_deprecated_tls_is_medium_or_high():
    score, risk = score_issues(["Deprecated TLS version detected: TLSv1"])
    assert score >= 3
    assert risk in ["MEDIUM", "HIGH"]


def test_multiple_issues_is_high_risk():
    issues = [
        "Deprecated TLS version detected: TLSv1",
        "Weak cipher detected: RC4",
        "No certificate presented"
    ]

    score, risk = score_issues(issues)

    assert score >= 6
    assert risk == "HIGH"