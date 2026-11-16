from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext as _

from .base import AbstractUserOwnedModel, TimestampedMixin


class Quote(AbstractUserOwnedModel):
    STR_MAX_LENGTH = 30

    text = models.TextField(
        verbose_name=_('Text'),
    )
    source = models.ForeignKey(
        'Source',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'text'],
                name='%(app_label)s_%(class)s_user_text_uniq',
            ),
        ]

    def __str__(self) -> str:
        return truncatechars(self.text, self.STR_MAX_LENGTH)


class DefinitionQuote(TimestampedMixin):
    definition = models.ForeignKey(
        'Definition',
        on_delete=models.PROTECT,
    )
    quote = models.ForeignKey(
        Quote,
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['definition', 'quote'],
                name='%(app_label)s_%(class)s_definition_quote_uniq',
            )
        ]
