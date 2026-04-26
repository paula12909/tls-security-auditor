from src.auditor import parse_target


def test_parse_target():
    host, port = parse_target("localhost:8080")
    assert host == "localhost"
    assert port == 8080