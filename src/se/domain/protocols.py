"""Protocols for domain interface."""

from typing import Protocol

# Value-objects


class HasDefinition(Protocol):
    @property
    def definition(self) -> str: ...


class HasExplanation(Protocol):
    @property
    def explanation(self) -> str: ...


class PresentationCardProto(
    HasDefinition,
    HasExplanation,
    Protocol,
): ...


# Entities


class PresentationDomainProto(Protocol):
    def create_card(self) -> PresentationCardProto: ...
