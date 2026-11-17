"""Protocols for api client interfaces."""

from typing import Protocol


class PresentationApiProto[CardT](Protocol):
    def get_card(self) -> CardT: ...
