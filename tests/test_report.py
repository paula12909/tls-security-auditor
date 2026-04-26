from src.report import write_json


def test_write_json(tmp_path):
    data = [{"test": 1}]

    # temporarily override output directory
    import src.report as report
    report.ARTIFACT_DIR = tmp_path

    write_json(data)

    assert (tmp_path / "results.json").exists()