from django.contrib import admin

from .models import Definition


@admin.register(Definition)
class DefinitionAdmin(admin.ModelAdmin): ...
