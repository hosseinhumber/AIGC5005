"""Recording what a run used, so someone else can repeat it."""

import json
import platform
import sys
from importlib import metadata
from pathlib import Path

from .config import Settings

TOOLS = ("pytest", "mypy", "ruff")


def describe_environment() -> dict[str, str]:
    """Return the Python version, the operating system and the tool versions."""
    versions = {"python": platform.python_version(), "system": platform.system()}
    for name in TOOLS:
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = "not installed"
    return versions


def write_run_info(path: Path, settings: Settings) -> None:
    """Save the settings and the environment next to the results."""
    info = {
        "interpreter": sys.executable,
        "environment": describe_environment(),
        "settings": {
            "data_file": str(settings.data_file),
            "seed": settings.seed,
            "sample_size": settings.sample_size,
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(info, indent=2), encoding="utf-8")
