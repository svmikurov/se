"""Presentation microservice tests."""

from se.application.presentation import PresentationUseCaseProto
from se.domain.protocols import PresentationCardProto


def test_use_case_returns_card(
    use_case: PresentationUseCaseProto,
    presentation_card: PresentationCardProto,
) -> None:
    card = use_case.handle()
    assert card == presentation_card
