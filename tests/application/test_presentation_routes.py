"""Presentation REST API tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from se.application.presentation.main import app

if TYPE_CHECKING:
    from unittest.mock import Mock

    from fastapi.testclient import TestClient


def test_read_item(client: TestClient, mock_term_repo: Mock) -> None:
    with app.container.in_memory_repository.override(mock_term_repo):  # type: ignore[attr-defined]
        response = client.get('/presentation/')

    assert response.status_code == 200
    term_presentation_card = response.json()['presentation']
    assert 'definition_' in term_presentation_card['definition']
    assert 'explanation_' in term_presentation_card['explanation']
