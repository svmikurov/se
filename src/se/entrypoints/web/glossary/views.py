from __future__ import annotations

from typing import TYPE_CHECKING, Any

from dependency_injector.wiring import Provide, inject
from django.views.generic.base import TemplateView

from se.entrypoints.web.di import Container

if TYPE_CHECKING:
    from django.http.request import HttpRequest
    from django.http.response import HttpResponseBase

    from se.domain.protocols import PresentationCardProto

    from ..handlers.protocols import RequestHandlerProto

    type _RequestHandlerT = RequestHandlerProto[PresentationCardProto]


class IndexView(TemplateView):
    template_name = 'index.html'


class PresentationView(TemplateView):
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

    @property
    def use_case(self) -> _RequestHandlerT:
        if self._request_handler is None:
            raise AttributeError('UseCase not initialized')
        return self._request_handler

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['definition_text'] = 'Definition text' 
        data['explanation_text'] = 'Explanation text' 
        return data
