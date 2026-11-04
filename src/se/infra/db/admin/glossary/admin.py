from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from . import forms, models


@admin.register(models.Definition)
class DefinitionAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        'text',
        'created_at',
    )


@admin.register(models.Explanation)
class ExplanationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        'text',
        'source',
        'created_at',
    )


@admin.register(models.Term)
class TermAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    form = forms.TermForm
    list_display = (
        'definition',
        'explanation',
        'created_at',
    )

    def get_form(
        self,
        request: HttpRequest,
        obj: models.Term | None = None,
        change: bool = False,
        **kwargs: Any,
    ) -> type[forms.TermForm]:
        form_class = super().get_form(request, obj, change, **kwargs)
        owner = obj.user if obj and obj.pk else request.user

        class _BoundTermForm(form_class):  # type: ignore[misc, valid-type]
            def __init__(self, *args: Any, **kw: Any) -> None:
                kw.setdefault('owner', owner)
                super().__init__(*args, **kw)

        return _BoundTermForm


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]
