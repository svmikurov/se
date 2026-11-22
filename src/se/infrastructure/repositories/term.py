"""Term repository."""

from typing import Any

from se.domain import TermProto

from .abstract import AddRepository, ListRepository


class InMemoryTermRepository(
    AddRepository[TermProto],
    ListRepository[TermProto],
):
    def __init__(self) -> None:
        self._terms: set[TermProto] = set()

    def add(self, items: list[TermProto]) -> None:
        self._terms.update(items)

    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[TermProto]:
        return list(self._terms)
