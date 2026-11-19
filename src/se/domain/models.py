from .protocols import PresentationCardProto
from .values import PresentationCard


class PresentationDomain:
    def create_card(self) -> PresentationCardProto:
        """Create presentation card."""
        return PresentationCard(
            definition='Definition text',
            explanation='Explanation text',
        )
