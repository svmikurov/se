from django.contrib import admin

from . import models


@admin.register(models.Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = [
        'native',
        'foreign',
    ]
    