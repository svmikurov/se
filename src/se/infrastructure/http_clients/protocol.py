"""Protocols for HTTP Client interface."""

from typing import Any, Callable, Protocol


class HasJson(Protocol):
    @property
    def json(self) -> Callable[[], dict[str, Any]]: ...


class HttpClientProto(
    HasJson,
    Protocol,
):
    def get(self, *args: object, **kwargs: object) -> HasJson: ...
