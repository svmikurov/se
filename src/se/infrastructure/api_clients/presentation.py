"""Presentation Service API client."""

import os
from urllib.parse import urljoin

from se.infrastructure.api_clients.schemas import PresentationCard
from se.infrastructure.http_client.protocol import HttpClientProto

# FIXME: Relocate url to settings, inject settings to API client
_base_url = os.getenv('PRESENTATION_SERVICE_URL', '').strip()
if not _base_url:
    raise RuntimeError(
        'PRESENTATION_SERVICE_URL environment variable is not set'
    )
PRESENTATION_URL = urljoin(f'{_base_url.rstrip("/")}/', 'presentation/')


class PresentationApi:
    def __init__(
        self,
        http_client: HttpClientProto,
    ) -> None:
        self._http_client = http_client

    def get_card(self) -> PresentationCard:
        response = self._http_client.get(PRESENTATION_URL)
        payload = response.json()
        return PresentationCard(
            definition=payload['presentation']['definition'],
            explanation=payload['presentation']['explanation'],
        )
