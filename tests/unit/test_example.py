"""Test data loading and processing."""

from __future__ import annotations

from pathlib import Path

import pytest


class TestLoad:
    """Test data loading and processing."""

    @pytest.fixture(scope="class")
    def data_f(self) -> Path:
        """Folder to write model files to."""
        return (Path(__file__).parent / "../data").resolve()

    @pytest.fixture(scope="class")
    def text(self, data_f: Path) -> str:
        """Load in the datasets used for training."""
        with open(data_f / "example.txt") as f:
            text = f.read().strip()
        return text

    def test_example(self, text: str) -> None:
        """Test the loading of the regular dataset splits."""
        assert "Hello" in text
        assert "World" in text
