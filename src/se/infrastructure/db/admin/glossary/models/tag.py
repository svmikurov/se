from django.db import models
from django.utils.translation import gettext as _

from ...core.models import (
    AbstractUserOwnedModel,
    TimestampedMixin,
)


class Tag(AbstractUserOwnedModel):
    TAG_MAX_LENGTH = 70

    name = models.CharField(
        max_length=TAG_MAX_LENGTH,
        verbose_name=_('Name'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='%(app_label)s_%(class)s_user_name_uniq',
            ),
        ]

    def __str__(self) -> str:
        return self.name


class DefinitionTag(TimestampedMixin):
    definition = models.ForeignKey(
        'Definition',
        on_delete=models.CASCADE,
        related_name='tag_links',
    )
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        related_name='definition_links',
    )

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['definition', 'tag'],
                name='%(app_label)s_%(class)s_definition_tag_uniq',
            ),
        ]
