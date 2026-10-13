"""Settings read from a TOML file."""

import tomllib
from dataclasses import dataclass
from pathlib import Path

from .errors import ConfigError


@dataclass(frozen=True)
class Settings:
    """Everything that can change between runs without changing the code."""

    data_file: Path
    output_dir: Path
    seed: int
    sample_size: int
    log_level: str


def load_settings(path: Path) -> Settings:
    """Read the settings file, raising ConfigError if it is missing or incomplete."""
    try:
        with path.open("rb") as handle:
            raw = tomllib.load(handle)
    except OSError as error:
        raise ConfigError(
            f"Cannot read the settings file {path}: {error.strerror}"
        ) from error
    except tomllib.TOMLDecodeError as error:
        raise ConfigError(f"{path} is not valid TOML: {error}") from error
    try:
        return Settings(
            data_file=Path(raw["data_file"]),
            output_dir=Path(raw["output_dir"]),
            seed=int(raw["seed"]),
            sample_size=int(raw["sample_size"]),
            log_level=str(raw.get("log_level", "INFO")).upper(),
        )
    except KeyError as error:
        raise ConfigError(f"{path} is missing the setting {error}.") from error
