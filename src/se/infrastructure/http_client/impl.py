"""HTTP Client."""

import logging
from typing import Literal

import httpx

log = logging.getLogger(__name__)


class HttpClient:
    def __init__(self) -> None:
        self._client = httpx.Client()

    def _request(
        self,
        method: Literal['get'],
        url: str,
    ) -> httpx.Response:
        response = self._client.request(method, url)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            msg = (
                f'Got response {response.status_code} status '
                f"from '{response.url.path}'\n"
            )
            log.error(msg)
            raise

        return response

    def get(self, url: str) -> httpx.Response:
        log.error(f'HTTP request to {url}')
        return self._client.get(url)
