from __future__ import annotations

from typing import TYPE_CHECKING

from se.domain import NoItemsForExercise

if TYPE_CHECKING:
    from se.domain.protocols import (
        PresentationCardProto,
        PresentationDomainProto,
        TermProto,
    )

    from . import PresentationRepositoryProto


class PresentationUseCase:
    def __init__(
        self,
        domain: PresentationDomainProto[TermProto],
        repo: PresentationRepositoryProto[TermProto],
    ) -> None:
        self._domain = domain
        self._repo = repo

    def handle(self) -> PresentationCardProto | None:
        terms: list[TermProto] = self._repo.list()
        try:
            term_presentation_card = self._domain.create_card(terms)
        except NoItemsForExercise:
            return None
        return term_presentation_card
