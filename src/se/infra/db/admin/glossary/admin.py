from django.contrib import admin

from . import models


@admin.register(models.Definition)
class DefinitionAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


@admin.register(models.Explanation)
class ExplanationAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


@admin.register(models.Term)
class TermAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]
