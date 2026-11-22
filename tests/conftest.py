from __future__ import annotations

import os
from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from se.application.presentation import PresentationRepositoryProto
from se.application.presentation.main import app
from se.application.presentation.use_cases import PresentationUseCase
from se.domain import PresentationCard, PresentationDomain, Term
from se.infrastructure.repositories import InMemoryTermRepository

if TYPE_CHECKING:
    from typing import Any, Generator

    from se.application.presentation import (
        HasList,
        PresentationUseCaseProto,
    )
    from se.domain import (
        PresentationCardProto,
        PresentationDomainProto,
        TermProto,
    )

pytest_plugins = [
    'tests.fixtures.db',
]


# Required at import time by presentation api until URL
# is moved to Settings (see FIXME in api_client/presentation.py)
os.environ.setdefault('PRESENTATION_SERVICE_URL', 'http://presentation:8000')


# Test data


@pytest.fixture
def term_items() -> list[dict[str, Any]]:
    term_count = 3
    return [
        {
            'id': id,
            'definition': f'definition_{id}',
            'explanation': f'explanation_{id}',
        }
        for id in range(1, term_count + 1)
    ]


# Domain


@pytest.fixture
def presentation_domain() -> PresentationDomainProto[TermProto]:
    return PresentationDomain()


@pytest.fixture
def presentation_card() -> PresentationCardProto:
    return PresentationCard(
        definition='Definition text',
        explanation='Explanation text',
    )


# Infrastructure


@pytest.fixture(scope='module')
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def in_memory_term_repo() -> HasList[TermProto]:
    return InMemoryTermRepository()


@pytest.fixture
def mock_term_repo(term_items: list[dict[str, Any]]) -> Mock:
    mock = Mock(spec=PresentationRepositoryProto)
    mock.list.return_value = [Term(**data) for data in term_items]
    return mock


# Application (Services)


@pytest.fixture
def use_case(
    presentation_domain: PresentationDomainProto[TermProto],
    in_memory_term_repo: PresentationRepositoryProto[TermProto],
) -> PresentationUseCaseProto:
    return PresentationUseCase(
        domain=presentation_domain,
        repo=in_memory_term_repo,
    )
