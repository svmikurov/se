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

    def handle(self) -> PresentationCardProto:
        terms = self._repo.list()
        return self._domain.create_card(terms)
