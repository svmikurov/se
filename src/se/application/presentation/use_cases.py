from se.domain.protocols import PresentationCardProto, PresentationDomainProto

from . import PresentationRepositoryProto


class PresentationUseCase:
    def __init__(
        self,
        domain: PresentationDomainProto,
        repo: PresentationRepositoryProto[PresentationCardProto],
    ) -> None:
        self._domain = domain
        self._repo = repo

    def handle(self) -> PresentationCardProto:
        return self._domain.create_card()
