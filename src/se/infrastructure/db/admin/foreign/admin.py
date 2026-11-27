from django.contrib import admin

from . import models
from ..core.models import SaveModelWithUserMixin


@admin.register(models.Translation)
class TranslationAdmin(SaveModelWithUserMixin, admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = [
        'native',
        'foreign',
    ]
    exclude = ('user',)
