"""Base views."""

from typing import Any

from django.views.generic.base import ContextMixin

from se.entrypoints.web.core.handlers.protocols import RequestHandlerProto


class RequestHandlerMixin[HandlerResultT](ContextMixin):
    _request_handler: RequestHandlerProto[HandlerResultT]

    @property
    def request_handler(self) -> RequestHandlerProto[HandlerResultT]:
        if self._request_handler is None:
            raise AttributeError('UseCase not initialized')
        return self._request_handler

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return {**context, **self.get_handler_data()}

    def get_handler_data(self) -> dict[str, Any]:
        return dict()
