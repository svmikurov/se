"""Presentation Service API client."""

from se.infrastructure.api_clients.schemas import PresentationCard
from se.infrastructure.http_clients import HttpClientProto


class PresentationApi:
    def __init__(
        self,
        http_client: HttpClientProto,
    ) -> None:
        self._http_client = http_client

    def get_card(self) -> PresentationCard:
        payload = self._http_client.get()
        return PresentationCard(
            definition=payload['definition'],
            explanation=payload['explanation'],
        )
