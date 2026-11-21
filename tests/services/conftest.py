from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from se.application.presentation.main import app
from se.application.presentation.use_cases import PresentationUseCase
from se.domain.models import PresentationDomain
from se.domain.values import PresentationCard
from se.infrastructure.repositories.term import InMemoryTermRepository

if TYPE_CHECKING:
    from typing import Any, Generator

    from se.application.protocols import HasList, PresentationUseCaseProto
    from se.domain import Term
    from se.domain.protocols import (
        PresentationCardProto,
        PresentationDomainProto,
    )


# Test data


@pytest.fixture
def terms_data() -> list[dict[str, Any]]:
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
def presentation_domain() -> PresentationDomainProto:
    return PresentationDomain()


@pytest.fixture
def presentation_card() -> PresentationCardProto:
    return PresentationCard(
        definition='Definition text',
        explanation='Explanation text',
    )


# Application


@pytest.fixture
def use_case(
    presentation_domain: PresentationDomainProto,
) -> PresentationUseCaseProto:
    return PresentationUseCase(domain=presentation_domain)


@pytest.fixture(scope='module')
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


# Infrastructure


@pytest.fixture
def in_memory_term_repo() -> HasList[Term]:
    return InMemoryTermRepository()
