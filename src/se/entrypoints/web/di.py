from dependency_injector import containers, providers
from httpx import Client

from se.infrastructure.api_clients.presentation import PresentationApi

from .handlers import PresentationRequestHandler


class Container(containers.DeclarativeContainer):
    http_client = providers.Factory(Client)

    presentation_client_api = providers.Factory(
        PresentationApi,
        http_client=http_client,
    )
    presentation_handler = providers.Factory(
        PresentationRequestHandler,
        client_api=presentation_client_api,
    )
