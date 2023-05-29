"""Setup module for this Python package."""

from __future__ import annotations

from pathlib import Path

from setuptools import find_packages, setup


def load_dependencies(tag: str) -> list[str]:
    """Load the dependencies from the specified requirements file."""
    with open(Path(__file__).parent / f"requirements.{tag}.txt") as f:
        requirements = [
            line.strip() for line in f.readlines() if line.strip() and (line[0] != "#")
        ]
    return requirements


# List all possible dependencies
run_dependencies = load_dependencies("run")
dev_dependencies = load_dependencies("dev")

# Install
setup(
    name="my_package",
    version="0.0.0",
    description="Pixel level crop classification using deep learning.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=run_dependencies,
    include_package_data=True,
    extras_require={
        "dev": dev_dependencies,
    },
)
