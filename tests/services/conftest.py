import pytest

from se.application.presentation.use_cases import PresentationUseCase
from se.application.protocols import PresentationUseCaseProto
from se.domain.models import PresentationDomain
from se.domain.protocols import PresentationCardProto, PresentationDomainProto
from se.domain.values import PresentationCard


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
