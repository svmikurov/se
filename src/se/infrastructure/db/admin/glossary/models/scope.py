from django.db import models
from django.utils.translation import gettext as _

from se.infrastructure.db.admin.core.models import (
    AbstractUserOwnedModel,
    TimestampedMixin,
)


class Scope(AbstractUserOwnedModel):
    NAME_MAX_LENGTH = 70

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name=_('Name'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='%(app_label)s_%(class)s_user_name_uniq',
            )
        ]

    def __str__(self) -> str:
        return self.name


class DefinitionScope(TimestampedMixin):
    scope = models.ForeignKey(
        'Scope',
        on_delete=models.PROTECT,
        related_name='definition_links',
    )

    definition = models.ForeignKey(
        'Definition',
        on_delete=models.PROTECT,
        related_name='scope_links',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['scope', 'definition'],
                name='%(app_label)s_%(class)s_definition_scope_uniq',
            )
        ]
