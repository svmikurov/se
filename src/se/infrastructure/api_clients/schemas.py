"""Service API client schemas."""

from dataclasses import dataclass


@dataclass
class PresentationCard:
    definition: str
    explanation: str
