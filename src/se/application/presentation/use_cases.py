from se.domain.protocols import PresentationCardProto, PresentationDomainProto


class PresentationUseCase:
    def __init__(self, domain: PresentationDomainProto) -> None:
        self._domain = domain

    def handle(self) -> PresentationCardProto:
        return self._domain.create_card()
