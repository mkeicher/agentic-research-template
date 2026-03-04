"""Shared test fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture()
def data_root(tmp_path):
    """Provide a temporary data root directory for tests."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture(autouse=True)
def _isolate_env(monkeypatch, tmp_path):
    """Ensure tests don't depend on real environment variables."""
    # [CUSTOMIZE: Use your project's data root env var name]
    monkeypatch.setenv("DATA_ROOT", str(tmp_path / "data"))
