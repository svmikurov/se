"""Protocols for domain interface."""

from typing import Protocol

# Model fields


class HasIdentifier(Protocol):
    @property
    def id(self) -> int: ...


class HasDefinition(Protocol):
    @property
    def definition(self) -> str: ...


class HasExplanation(Protocol):
    @property
    def explanation(self) -> str: ...


# Value-objects


class PresentationCardProto(
    HasDefinition,
    HasExplanation,
    Protocol,
): ...


# Entities


class TermProto(
    HasIdentifier,
    HasDefinition,
    HasExplanation,
    Protocol,
): ...


# Services


class PresentationDomainProto[Item](Protocol):
    def create_card(self, items: list[Item]) -> PresentationCardProto: ...
