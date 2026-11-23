from typing import Any, Protocol

from se.domain import Displayed

# Use cases


class PresentationUseCaseProto(Protocol):
    def handle(self) -> Displayed | None: ...


# Repositories


class HasAdd[Item](Protocol):
    def add(self, items: list[Item]) -> None: ...


class HasList[Item](Protocol):
    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[Item]: ...


class TermRepositoryProto[Item](
    HasAdd[Item],
    HasList[Item],
    Protocol,
): ...


class CardRepositoryProto[Item, Card](Protocol):
    def get_card(self, item: Item) -> Card: ...
