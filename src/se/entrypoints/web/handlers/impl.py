"""Request handler."""

from dataclasses import dataclass


@dataclass
class PresentationCard:
    definition: str
    explanation: str


class RequestHandler:
    def handle(self) -> PresentationCard:
        return PresentationCard(
            definition='Definition text',
            explanation='Explanation text',
        )
