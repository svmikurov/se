"""Protocols for HTTP Client interface."""

from typing import Any, Protocol


class HttpClientProto(Protocol):
    def get(self, *args: object, **kwargs: object) -> dict[str, Any]: ...
