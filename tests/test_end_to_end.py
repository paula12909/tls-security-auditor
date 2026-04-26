from src.checks import run_checks
from src.scoring import score_issues


def test_happy_path_low_risk():
    result = {
        "tls_version": "TLSv1.3",
        "cipher": "TLS_AES_256_GCM_SHA384",
        "certificate_present": True,
        "self_signed": False,
        "error": None
    }

    policy = {
        "minimum_tls_version": "TLSv1.2",
        "disallowed_ciphers": ["RC4", "3DES", "DES", "NULL"],
        "allow_self_signed": False
    }

    issues = run_checks(result, policy)
    score, risk = score_issues(issues)

    assert issues == []
    assert score == 0
    assert risk == "LOW"


def test_negative_path_high_risk():
    result = {
        "tls_version": "TLSv1",
        "cipher": "RC4",
        "certificate_present": False,
        "self_signed": False,
        "error": None
    }

    policy = {
        "minimum_tls_version": "TLSv1.2",
        "disallowed_ciphers": ["RC4", "3DES", "DES", "NULL"],
        "allow_self_signed": False
    }

    issues = run_checks(result, policy)
    score, risk = score_issues(issues)

    assert len(issues) >= 2
    assert risk == "HIGH"