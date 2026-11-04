from django.db import models
from django.utils.translation import gettext as _

from .base import AbstractUserOwnedModel
from .source import Source


class Definition(AbstractUserOwnedModel):
    DEFINITION_MAX_LENGTH = 70
    ABBREVIATION_MAX_LENGTH = 10

    text = models.CharField(
        max_length=DEFINITION_MAX_LENGTH,
        verbose_name=_('Text'),
    )
    abbreviation = models.CharField(
        max_length=ABBREVIATION_MAX_LENGTH,
        verbose_name=_('Abbreviation'),
        null=True,
        blank=True,
    )
    translation = models.CharField(
        max_length=DEFINITION_MAX_LENGTH,
        verbose_name=_('Translation'),
        null=True,
        blank=True,
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
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        verbose_name=_('Source'),
        null=True,
        blank=True,
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


class Term(AbstractUserOwnedModel):
    definition = models.ForeignKey(
        Definition,
        on_delete=models.CASCADE,
        verbose_name=_('Term definition'),
    )
    explanation = models.ForeignKey(
        Explanation,
        on_delete=models.CASCADE,
        verbose_name=_('Term explanation'),
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['definition', 'explanation'],
                name='%(app_label)s_definition_explanation_uniq',
            ),
        ]

    def __str__(self) -> str:
        return str(self.definition)
