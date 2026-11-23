"""Protocols for exercise domain interface."""

from typing import Protocol

# Model fields


class HasID(Protocol):
    @property
    def id(self) -> int: ...


class HasDefinitionID(Protocol):
    @property
    def definition_id(self) -> int: ...


class HasMeaningID(Protocol):
    @property
    def meaning_id(self) -> int: ...


class HasDefinition(Protocol):
    @property
    def definition(self) -> str: ...


class HasMeaning(Protocol):
    @property
    def meaning(self) -> int: ...


class HasQuestion(Protocol):
    @property
    def question(self) -> str: ...


class HasAnswer(Protocol):
    @property
    def answer(self) -> str: ...


# Value-objects


class Displayed(
    HasDefinition,
    HasMeaning,
    Protocol,
): ...


# Entities


class Learnable(
    HasID,
    HasDefinitionID,
    HasMeaningID,
    Protocol,
): ...


# Services


class PresentationProto(Protocol):
    def choose(self, contenders: list[Learnable]) -> Learnable: ...
