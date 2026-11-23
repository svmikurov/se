from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Case:
    definition_id: int
    meaning_id: int


@dataclass(frozen=True, slots=True)
class Card:
    definition: str
    meaning: str
