"""Collect the files a Hugging Face Space needs into space_upload/.

Run it from this folder after python churn_model.py:  python prepare_space.py
It writes requirements.txt with the versions installed here, and checks that the
scikit-learn version matches the one recorded when the model was saved.
"""

import json
import shutil
from importlib.metadata import version
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "space_upload"
FILES = ["app.py", "predict.py", "churn_model.joblib"]
PACKAGES = ["scikit-learn", "pandas", "joblib"]


def requirements_text() -> str:
    """Return requirements.txt lines with exact versions of what is installed."""
    return "".join(f"{name}=={version(name)}\n" for name in PACKAGES)


def check_model_version() -> None:
    """Stop if the saved model came from a different scikit-learn version."""
    recorded = json.loads((HERE / "metrics.json").read_text())["scikit_learn"]
    if recorded != version("scikit-learn"):
        raise SystemExit(
            f"The model was saved by scikit-learn {recorded}, but "
            f"{version('scikit-learn')} is installed. "
            "Run python churn_model.py again in this environment."
        )


def main() -> None:
    check_model_version()
    OUT.mkdir(exist_ok=True)
    for name in FILES:
        shutil.copy(HERE / name, OUT / name)
    (OUT / "requirements.txt").write_text(requirements_text(), encoding="utf-8")
    shutil.copy(HERE / "space_README_template.md", OUT / "README.md")
    print("Wrote", ", ".join(sorted(p.name for p in OUT.iterdir())))
    print("Edit space_upload/README.md, then upload the five files to your Space.")


if __name__ == "__main__":
    main()
