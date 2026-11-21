"""Test stubs."""

from typing import Any

from se.infrastructure.http_clients.protocol import HasJson
from tests.fixtures.presentation import PRESENTATION_CARD


class FakeResponse:
    def json(self) -> dict[str, Any]:
        return {'presentation': PRESENTATION_CARD}


class FakeHttpClient:
    def get(self, *args: object, **kwargs: object) -> HasJson:
        return FakeResponse()
