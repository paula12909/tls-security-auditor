from src.checks import check_tls_version, check_cipher, check_certificate


def test_tls_version_passes_policy():
    result = {"tls_version": "TLSv1.3"}
    policy = {"minimum_tls_version": "TLSv1.2"}

    issues = check_tls_version(result, policy)

    assert issues == []


def test_tls_version_fails_policy():
    result = {"tls_version": "TLSv1"}
    policy = {"minimum_tls_version": "TLSv1.2"}

    issues = check_tls_version(result, policy)

    assert "Deprecated TLS version detected: TLSv1" in issues


def test_missing_cipher_detected():
    result = {"cipher": None}
    policy = {"disallowed_ciphers": ["RC4"]}

    issues = check_cipher(result, policy)

    assert "No cipher detected" in issues


def test_missing_certificate_detected():
    result = {"certificate_present": False, "self_signed": False}
    policy = {"allow_self_signed": False}

    issues = check_certificate(result, policy)

    assert "No certificate presented" in issues