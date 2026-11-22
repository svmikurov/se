from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from se.application.presentation.main import app
from se.application.presentation.use_cases import PresentationUseCase
from se.domain import PresentationCard, PresentationDomain
from se.infrastructure.repositories import InMemoryTermRepository

if TYPE_CHECKING:
    from typing import Any, Generator

    from se.application.presentation import (
        HasList,
        PresentationRepositoryProto,
        PresentationUseCaseProto,
    )
    from se.domain import (
        PresentationCardProto,
        PresentationDomainProto,
        Term,
        TermProto,
    )


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
def in_memory_term_repo() -> HasList[Term]:
    return InMemoryTermRepository()


# Application


@pytest.fixture
def use_case(
    presentation_domain: PresentationDomainProto[TermProto],
    in_memory_term_repo: PresentationRepositoryProto[TermProto],
) -> PresentationUseCaseProto:
    return PresentationUseCase(
        domain=presentation_domain,
        repo=in_memory_term_repo,
    )
