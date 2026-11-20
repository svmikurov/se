from __future__ import annotations

from typing import TYPE_CHECKING, Generator

import pytest
from fastapi.testclient import TestClient

from se.application.presentation.app import app
from se.application.presentation.use_cases import PresentationUseCase
from se.domain.models import PresentationDomain
from se.domain.values import PresentationCard

if TYPE_CHECKING:
    from se.application.protocols import PresentationUseCaseProto
    from se.domain.protocols import (
        PresentationCardProto,
        PresentationDomainProto,
    )


@pytest.fixture(scope='module')
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def presentation_card() -> PresentationCardProto:
    return PresentationCard(
        definition='Definition text',
        explanation='Explanation text',
    )


@pytest.fixture
def presentation_domain() -> PresentationDomainProto:
    return PresentationDomain()


@pytest.fixture
def use_case(
    presentation_domain: PresentationDomainProto,
) -> PresentationUseCaseProto:
    return PresentationUseCase(domain=presentation_domain)
