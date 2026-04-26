from src.compare import compare_results


def test_compare_basic():
    results = [
        {"host": "a", "port": 1, "risk_score": 5, "risk_level": "HIGH"},
        {"host": "b", "port": 2, "risk_score": 1, "risk_level": "LOW"}
    ]

    output = compare_results(results)

    assert "more secure" in output.lower()