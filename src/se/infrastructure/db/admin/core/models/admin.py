"""Administration mixins."""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.template.defaultfilters import truncatechars

if TYPE_CHECKING:
    from django.db.models import Model
    from django.forms import Form
    from django.http import HttpRequest

TRUNCATE_LENGTH = 40


class SaveModelWithUserMixin:
    def save_model(
        self,
        request: HttpRequest,
        obj: Model,
        form: Form,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:  # type: ignore[attr-defined]
            obj.user = request.user  # type: ignore[attr-defined]
        super().save_model(request, obj, form, change)  # type: ignore[misc]


class ShowShortTextMixin:
    def short_text(self, obj: Model) -> str:
        return truncatechars(obj.text, TRUNCATE_LENGTH)  # type: ignore[attr-defined]
