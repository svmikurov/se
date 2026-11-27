from django.contrib import admin

from . import models


@admin.register(models.Translation)
class TranslationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = [
        'native',
        'foreign',
    ]
