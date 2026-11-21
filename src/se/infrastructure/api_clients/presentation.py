"""Presentation Service API client."""

import os

from se.infrastructure.api_clients.schemas import PresentationCard
from se.infrastructure.http_clients import HttpClientProto


class PresentationApi:
    def __init__(
        self,
        http_client: HttpClientProto,
    ) -> None:
        self._http_client = http_client

    def get_card(self) -> PresentationCard:
        url = os.getenv('PRESENTATION_SERVICE_URL')
        response = self._http_client.get(f'{url}/presentation')
        payload = response.json()
        return PresentationCard(
            definition=payload['presentation']['definition'],
            explanation=payload['presentation']['explanation'],
        )
