"""Request handler."""

from se.infrastructure.api_clients.protocols import PresentationApiProto
from se.infrastructure.api_clients.schemas import PresentationCard


class PresentationRequestHandler:
    def __init__(
        self,
        client_api: PresentationApiProto[PresentationCard],
    ) -> None:
        self._client = client_api

    def handle(self) -> PresentationCard:
        card = self._client.get_card()
        return card
