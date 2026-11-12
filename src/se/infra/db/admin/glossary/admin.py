from typing import Any

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.template.defaultfilters import truncatechars
from django.utils import timezone

from . import models

TRUNCATE_LENGTH = 40


class SaveModelWithUserMixin:
    def save_model(
        self,
        request: HttpRequest,
        obj: Any,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)  # type: ignore[misc]


# Term


@admin.register(models.Definition)
class DefinitionAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
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

    def save_model(
        self,
        request: HttpRequest,
        obj: models.Definition,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:  # type: ignore[attr-defined]
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Explanation)
class ExplanationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ('text', 'source', 'created_at')
    search_fields = ('text',)
    exclude = ('user',)

    def save_model(
        self,
        request: HttpRequest,
        obj: models.Explanation,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:  # type: ignore[attr-defined]
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Term)
class TermAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
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

    def save_model(
        self,
        request: HttpRequest,
        obj: models.Term,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:  # type: ignore[attr-defined]
            obj.user = request.user
        super().save_model(request, obj, form, change)

    @admin.display(description='Explanation')
    def explanation_short(self, obj: models.Term) -> str:
        text = str(obj.explanation) if obj.explanation is not None else ''
        return truncatechars(text, TRUNCATE_LENGTH) or '-'

    @admin.display(description='Created', ordering='created_at')
    def created_short(self, obj: models.Term) -> str:
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d')


@admin.register(models.TermLink)
class TermLinkAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
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

    def save_model(
        self,
        request: HttpRequest,
        obj: models.TermLink,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:  # type: ignore[attr-defined]
            obj.user = request.user
        super().save_model(request, obj, form, change)


# Quote


@admin.register(models.Quote)
class QuoteAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    exclude = ('user',)


# Source


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


# Scope


@admin.register(models.Scope)
class ScopeAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    exclude = ('user',)

    def save_model(
        self,
        request: HttpRequest,
        obj: Any,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.DefinitionScope)
class DefinitionScopeAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


# Tag


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ('name',)
    exclude = ('user',)

    def save_model(
        self,
        request: HttpRequest,
        obj: Any,
        form: Any,
        change: bool,
    ) -> None:
        if not change and not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.DefinitionTag)
class DefinitionTagAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]
