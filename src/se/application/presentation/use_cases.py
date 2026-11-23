from __future__ import annotations

from typing import TYPE_CHECKING

from se.domain import NoItemsForExercise

if TYPE_CHECKING:
    from se.domain.protocols import (
        Displayed,
        Learnable,
        PresentationProto,
    )

    from . import (
        CardRepositoryProto,
        HasList,
    )


class PresentationUseCase:
    def __init__(
        self,
        domain: PresentationProto,
        term_repo: HasList[Learnable],
        card_repo: CardRepositoryProto[Learnable, Displayed],
    ) -> None:
        self._domain = domain
        self._term_repo = term_repo
        self._card_repo = card_repo

    def handle(self) -> Displayed | None:
        terms: list[Learnable] = self._term_repo.list()
        try:
            term_case = self._domain.choose(terms)
        except NoItemsForExercise:
            return None
        term_card = self._card_repo.get_card(term_case)
        return term_card
