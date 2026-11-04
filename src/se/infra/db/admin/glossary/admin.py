from django.contrib import admin

from .models import Definition, Explanation


@admin.register(Definition)
class DefinitionAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]


@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin): ...  # type: ignore[type-arg]
