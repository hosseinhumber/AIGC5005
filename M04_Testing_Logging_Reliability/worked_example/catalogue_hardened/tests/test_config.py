"""Tests for catalogue.config."""

from pathlib import Path

import pytest

from catalogue import ConfigError
from catalogue.config import load_settings


def test_settings_are_read(settings_file: Path) -> None:
    settings = load_settings(settings_file)
    assert settings.seed == 7
    assert settings.sample_size == 2
    assert settings.log_level == "INFO"


def test_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(ConfigError, match="Cannot read"):
        load_settings(tmp_path / "none.toml")


def test_missing_setting_is_named(tmp_path: Path) -> None:
    path = tmp_path / "partial.toml"
    path.write_text('data_file = "x.json"\n', encoding="utf-8")
    with pytest.raises(ConfigError, match="output_dir"):
        load_settings(path)


def test_invalid_toml_raises(tmp_path: Path) -> None:
    path = tmp_path / "bad.toml"
    path.write_text("this is = = not toml", encoding="utf-8")
    with pytest.raises(ConfigError, match="not valid TOML"):
        load_settings(path)
