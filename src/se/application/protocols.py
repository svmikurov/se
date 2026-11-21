from typing import Any, Protocol

from se.domain.protocols import PresentationCardProto

# Use cases


class PresentationUseCaseProto(Protocol):
    def handle(self) -> PresentationCardProto: ...


# Repositories


class HasAdd[Item](Protocol):
    def add(self, items: list[Item]) -> None: ...


class HasList[Item](Protocol):
    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[Item]: ...
