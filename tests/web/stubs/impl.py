"""Test stubs."""

from typing import Any

from ..fixtures.payload import PRESENTATION_CARD


class HttpClientStub:
    def get(self, *args: object, **kwargs: object) -> dict[str, Any]:
        return PRESENTATION_CARD
