"""Main tasks."""

import logging
import os
from pathlib import Path

from invoke import task

logger = logging.getLogger(__name__)
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@task
def lint(c):
    """Lint this package."""
    logger.info("Running pre-commit checks...")
    c.run("pre-commit run --all-files --color always", pty=True)


@task
def test(c):
    """Test this package."""
    logger.info("Running Pytest...")
    c.run(
        "env PYTHONPATH=src pytest --cov=src --cov-report term-missing --cov-report html:coverage/ tests",
        pty=True,
    )


@task
def lab(c):
    """Run Jupyter Lab."""
    notebooks_path = os.path.join(REPO_PATH, "notebooks")
    os.makedirs(notebooks_path, exist_ok=True)
    with c.cd(notebooks_path):
        c.run("jupyter lab --allow-root", pty=True)


@task
def docs(c, browser=False, output_dir="site"):
    """Generate this package's docs."""
    if browser:
        c.run("portray in_browser", pty=True)
    else:
        c.run(f"portray as_html --output_dir {output_dir} --overwrite", pty=True)
        logger.info("Package documentation available at ./site/index.html")


@task
def app(c, folder="models"):
    """Run Streamlit app."""
    logger.info("Opening streamlit application...")
    path = Path.home() / f"data/vito/crop_classification/{folder}"
    c.run(
        f"streamlit run application.py -- --folder={path}/",
        pty=True,
    )
