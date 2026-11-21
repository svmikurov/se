"""Term repository."""

from typing import Any

from se.domain import Term

from .abstract import AddRepository, ListRepository


class InMemoryTermRepository(
    AddRepository[Term],
    ListRepository[Term],
):
    def __init__(self) -> None:
        self._terms: set[Term] = set()

    def add(self, items: list[Term]) -> None:
        self._terms.update(items)

    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[Term]:
        return list(self._terms)
