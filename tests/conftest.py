from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from se.application.presentation.main import app

if TYPE_CHECKING:
    from typing import Callable, Generator


# HACK: Move presentation api URL to Settings
os.environ.setdefault('PRESENTATION_SERVICE_URL', 'http://presentation:8000')


@pytest.fixture(scope='module')
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def term_items_factory() -> Callable[[int], list[dict[str, int]]]:
    def _create_items(count: int = 3) -> list[dict[str, int]]:
        return [
            {'id': i, 'definition_id': i, 'explanation_id': i}
            for i in range(1, count + 1)
        ]

    return _create_items
