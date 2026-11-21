from __future__ import annotations

from typing import TYPE_CHECKING, override

from dependency_injector.wiring import Provide, inject
from django.views.generic.base import TemplateView

from se.domain.protocols import PresentationCardProto
from se.entrypoints.web.core.base.views import RequestHandlerMixin
from se.entrypoints.web.di import Container

if TYPE_CHECKING:
    from typing import Any

    from django.http.request import HttpRequest
    from django.http.response import HttpResponseBase

    from ..core.handlers.protocols import RequestHandlerProto

    type _RequestHandlerT = RequestHandlerProto[PresentationCardProto]


class IndexView(TemplateView):
    template_name = 'index.html'


class PresentationView(
    RequestHandlerMixin[PresentationCardProto],
    TemplateView,
):
    """Translation study test exercise view."""

    template_name = 'presentation.html'

    @inject
    def dispatch(
        self,
        request: HttpRequest,
        *args: object,
        request_handler: _RequestHandlerT = Provide[
            Container.presentation_handler
        ],
        **kwargs: object,
    ) -> HttpResponseBase:
        self._request_handler = request_handler
        return super().dispatch(request, *args, **kwargs)

    @override
    def get_handler_data(self) -> dict[str, Any]:
        data = super().get_handler_data()
        result = self.request_handler.handle()
        data['definition_text'] = result.definition
        data['explanation_text'] = result.explanation
        return data
