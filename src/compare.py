def compare_results(results: list) -> str:
    if len(results) < 2:
        return "Not enough targets to compare."

    first = results[0]
    second = results[1]

    lines = []
    lines.append("TLS Security Comparison")
    lines.append("=======================")
    lines.append(f"{first['host']}:{first['port']} -> {first['risk_level']} risk, score {first['risk_score']}")
    lines.append(f"{second['host']}:{second['port']} -> {second['risk_level']} risk, score {second['risk_score']}")

    if first["risk_score"] > second["risk_score"]:
        lines.append("Result: second target appears more secure.")
    elif first["risk_score"] < second["risk_score"]:
        lines.append("Result: first target appears more secure.")
    else:
        lines.append("Result: both targets have equal risk.")

    return "\n".join(lines)