from dataclasses import dataclass

from .exceptions import NoItemsForExercise
from .protocols import Learnable


@dataclass(frozen=True, slots=True)
class Term:
    id: int
    definition_id: int
    explanation_id: int


class PresentationDomain:
    def create_case(self, items: list[Learnable]) -> Learnable:
        """Create presentation case."""
        if not items:
            raise NoItemsForExercise
        term = items[-1]
        return term
