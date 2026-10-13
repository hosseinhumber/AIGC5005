"""Tests for the command line entry point."""

import json
from pathlib import Path

import pytest

from catalogue.main import main


def test_a_normal_run_prints_books_and_records_the_run(
    settings_file: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main(["--config", str(settings_file)])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Fluent Python" in output or "Clean Code" in output
    run_info = json.loads(
        (tmp_path / "out" / "run_info.json").read_text(encoding="utf-8")
    )
    assert run_info["settings"]["seed"] == 7


def test_a_missing_settings_file_exits_cleanly(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main(["--config", str(tmp_path / "none.toml")])
    assert exit_code == 1
    assert "Error: Cannot read the settings file" in capsys.readouterr().err


def test_a_missing_catalogue_exits_cleanly(
    settings_file: Path, catalogue_file: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    catalogue_file.unlink()
    exit_code = main(["--config", str(settings_file)])
    assert exit_code == 1
    assert "Cannot read the catalogue file" in capsys.readouterr().err
