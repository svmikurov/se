from typing import Protocol

from se.domain.protocols import PresentationCardProto


class PresentationUseCaseProto(Protocol):
    def handle(self) -> PresentationCardProto: ...
