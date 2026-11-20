"""Presentation REST API tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi.testclient import TestClient


def test_read_item(client: TestClient) -> None:
    data = {
        'definition': 'Definition text',
        'explanation': 'Explanation text',
    }

    response = client.get('/presentation/')

    assert response.status_code == 200
    content = response.json()
    assert content['presentation'] == data
