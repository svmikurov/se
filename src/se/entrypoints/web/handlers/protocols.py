"""Protocols for WEB BFF request handler interface."""

from typing import Protocol


class RequestHandlerProto[ResultT](Protocol):
    def handle(self) -> ResultT: ...
