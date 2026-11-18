"""Request handler tests."""

import pytest

from se.entrypoints.web.handlers import PresentationRequestHandler
from se.infrastructure.api_clients import PresentationApi
from se.infrastructure.http_clients import HttpClientProto

from ..fakes import FakeHttpClient
from ..fixtures.payload import PRESENTATION_CARD


@pytest.fixture
def http_client() -> HttpClientProto:
    return FakeHttpClient()


@pytest.fixture
def presentation_api(http_client: HttpClientProto) -> PresentationApi:
    return PresentationApi(http_client=http_client)


@pytest.fixture
def handler(presentation_api: PresentationApi) -> PresentationRequestHandler:
    return PresentationRequestHandler(client_api=presentation_api)


def test_handler_returns_card(handler: PresentationRequestHandler) -> None:
    card = handler.handle()
    assert card.definition == PRESENTATION_CARD['definition']
    assert card.explanation == PRESENTATION_CARD['explanation']
