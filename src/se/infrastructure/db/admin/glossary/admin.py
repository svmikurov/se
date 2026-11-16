from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib import admin
from django.db.models import QuerySet
from django.template.defaultfilters import truncatechars
from django.utils import timezone

from . import models

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


# Term


@admin.register(models.Definition)
class DefinitionAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        'text',
        'abbreviation',
        'translation',
        'user',
        'created_at',
    )
    search_fields = ('text', 'abbreviation', 'translation')
    list_filter = ('user',)
    exclude = ('user',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.Explanation)
class ExplanationAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ('text', 'source', 'created_at')
    search_fields = ('text',)
    exclude = ('user',)


@admin.register(models.Term)
class TermAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        'definition',
        'explanation_short',
        'created_short',
    )
    list_filter = ('user',)
    search_fields = ('definition__text', 'explanation__text')
    autocomplete_fields = ('definition', 'explanation')
    exclude = ('user',)
    readonly_fields = ('created_at', 'updated_at')

    @admin.display(description='Explanation')
    def explanation_short(self, obj: models.Term) -> str:
        text = str(obj.explanation) if obj.explanation is not None else ''
        return truncatechars(text, TRUNCATE_LENGTH) or '-'

    @admin.display(description='Created', ordering='created_at')
    def created_short(self, obj: models.Term) -> str:
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d')


@admin.register(models.TermLink)
class TermLinkAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        'parent',
        'child',
        'child__definition__translation',
    )
    list_filter = ('user',)
    search_fields = (
        'parent__definition__text',
        'child__definition__text',
    )
    autocomplete_fields = ('parent', 'child')
    exclude = ('user',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request: HttpRequest) -> QuerySet[models.TermLink]:
        return (
            super()
            .get_queryset(request)
            .select_related('parent', 'child', 'user')
        )


# Quote


@admin.register(models.Quote)
class QuoteAdmin(SaveModelWithUserMixin, ShowShortTextMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ['short_text', 'source']
    exclude = ('user',)


@admin.register(models.DefinitionQuote)
class DefinitionQuoteAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ['definition', 'quote']
    autocomplete_fields = ('definition',)


# Source


@admin.register(models.Source)
class SourceAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    exclude = ('user',)


@admin.register(models.Author)
class AuthorAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    exclude = ('user',)


# Scope


@admin.register(models.Scope)
class ScopeAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    exclude = ('user',)


@admin.register(models.DefinitionScope)
class DefinitionScopeAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    autocomplete_fields = ('definition',)


# Tag


@admin.register(models.Tag)
class TagAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ('name',)
    exclude = ('user',)


@admin.register(models.DefinitionTag)
class DefinitionTagAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]
