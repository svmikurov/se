from django.db import models
from django.utils.translation import gettext as _

from .base import AbstractUserOwnedModel


class Definition(AbstractUserOwnedModel):
    DEFINITION_MAX_LENGTH = 70

    text = models.CharField(
        max_length=DEFINITION_MAX_LENGTH,
        verbose_name=_('Text'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'text'],
                name='%(app_label)s_%(class)s_user_text_uniq',
            ),
        ]

    def __str__(self) -> str:
        return str(self.text)


class Explanation(AbstractUserOwnedModel):
    EXPLANATION_MAX_LENGTH = 200

    text = models.CharField(
        max_length=EXPLANATION_MAX_LENGTH,
        verbose_name=_('Text'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'text'],
                name='%(app_label)s_%(class)s_user_text_uniq',
            ),
        ]

    def __str__(self) -> str:
        return str(self.text)
