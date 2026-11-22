"""Presentation microservice tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from se.domain import Term

if TYPE_CHECKING:
    from typing import Any

    from se.application.presentation import (
        PresentationRepositoryProto,
        PresentationUseCaseProto,
    )
    from se.domain import TermProto


def test_use_case_returns_card(
    use_case: PresentationUseCaseProto,
    in_memory_term_repo: PresentationRepositoryProto[TermProto],
    term_items: list[dict[str, Any]],
) -> None:
    in_memory_term_repo.add([Term(**data) for data in term_items])

    card = use_case.handle()

    assert card is not None, 'Domain did not return presentation card'
    assert 'definition_' in card.definition
    assert 'explanation_' in card.explanation
