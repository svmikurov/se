from dataclasses import dataclass


@dataclass(frozen=True)
class PresentationCard:
    definition: str
    explanation: str
