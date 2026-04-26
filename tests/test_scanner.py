from src.scanner import scan_target


def test_invalid_port():
    try:
        scan_target("localhost", 70000)
        assert False
    except ValueError:
        assert True