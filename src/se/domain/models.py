from dataclasses import dataclass

from .exceptions import NoItemsForExercise
from .protocols import PresentationCardProto, TermProto
from .values import PresentationCard


@dataclass(frozen=True, slots=True)
class Term:
    id: int
    definition: str
    explanation: str


class PresentationDomain:
    def create_card(self, items: list[TermProto]) -> PresentationCardProto:
        """Create presentation card."""
        if not items:
            raise NoItemsForExercise
        term = items[-1]
        return PresentationCard(
            definition=term.definition,
            explanation=term.explanation,
        )
