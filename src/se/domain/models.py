from dataclasses import dataclass

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
        return PresentationCard(
            definition='Definition text',
            explanation='Explanation text',
        )
