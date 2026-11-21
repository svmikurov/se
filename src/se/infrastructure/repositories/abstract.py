"""Abstract base classes for repository."""

from abc import ABC, abstractmethod
from typing import Any


class AddRepository[Item](ABC):
    @abstractmethod
    def add(self, items: list[Item]) -> None: ...


class ListRepository[Item](ABC):
    @abstractmethod
    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[Item]: ...
