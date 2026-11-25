"""Author and source models."""

from django.db import models
from django.utils.translation import gettext as _

from ...core.models import AbstractUserOwnedModel


class Author(AbstractUserOwnedModel):
    """User-owned author; name unique per user."""

    AUTHOR_NAME_MAX_LENGTH = 70

    name = models.CharField(
        max_length=AUTHOR_NAME_MAX_LENGTH,
        verbose_name=_('Author name'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='%(app_label)s_%(class)s_user_author_uniq',
            )
        ]

    def __str__(self) -> str:
        return str(self.name)


class Source(AbstractUserOwnedModel):
    """User-owned source attributed to an author."""

    SOURCE_NAME_MAX_LENGTH = 200

    name = models.CharField(
        max_length=SOURCE_NAME_MAX_LENGTH, verbose_name=_('Source name')
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        verbose_name=_('Author'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'name'],
                name='%(app_label)s_%(class)s_author_name_uniq',
            ),
        ]

    def __str__(self) -> str:
        return str(self.name)
