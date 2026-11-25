from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from se.infrastructure.db.admin.core.models import AbstractUserOwnedModel
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
    EXPLANATION_MAX_LENGTH = 300

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
    definition = definition = models.ForeignKey(
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


class TermLink(AbstractUserOwnedModel):
    parent = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name='child_links',
        verbose_name=_('Parent term'),
    )
    child = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name='parent_links',
        verbose_name=_('Child term'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'child'],
                name='%(app_label)s_%(class)s_parent_child_uniq',
            ),
            models.CheckConstraint(
                condition=~models.Q(parent=models.F('child')),
                name='%(app_label)s_%(class)s_no_self_loop',
            ),
        ]
        verbose_name = _('Term link')
        verbose_name_plural = _('Term links')

    def __str__(self) -> str:
        return f'{self.parent} -> {self.child}'

    def clean(self) -> None:
        super().clean()
        if not self.parent_id or not self.child_id:  # type: ignore
            return
        if self.parent_id == self.child_id:  # type: ignore
            raise ValidationError(
                _('A term cannot be its own parent.'),
            )
        if self._creates_cycle():
            raise ValidationError(
                _('This link would create a cycle in the hierarchy.'),
            )

    def _creates_cycle(self) -> bool:
        seen: set[int] = set()
        stack: list[int] = [self.parent_id]  # type: ignore
        while stack:
            node_id = stack.pop()
            if node_id == self.child_id:  # type: ignore
                return True
            if node_id in seen:
                continue
            seen.add(node_id)
            stack.extend(
                TermLink.objects.filter(child_id=node_id).values_list(  # type: ignore
                    'parent_id', flat=True
                )
            )
        return False


class DefinitionLink(AbstractUserOwnedModel):
    parent = models.ForeignKey(
        Definition,
        on_delete=models.CASCADE,
        related_name='child_links',
        verbose_name=_('Parent definition'),
    )
    child = models.ForeignKey(
        Definition,
        on_delete=models.CASCADE,
        related_name='parent_links',
        verbose_name=_('Child definition'),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'child'],
                name='%(app_label)s_%(class)s_parent_child_uniq',
            ),
            models.CheckConstraint(
                condition=~models.Q(parent=models.F('child')),
                name='%(app_label)s_%(class)s_no_self_loop',
            ),
        ]
        verbose_name = _('Definition link')
        verbose_name_plural = _('Definition links')

    def __str__(self) -> str:
        return f'{self.parent} -> {self.child}'

    def clean(self) -> None:
        super().clean()
        if not self.parent_id or not self.child_id:  # type: ignore
            return
        if self.parent_id == self.child_id:  # type: ignore
            raise ValidationError(
                _('A definition cannot be its own parent.'),
            )
        if self._creates_cycle():
            raise ValidationError(
                _('This link would create a cycle in the hierarchy.'),
            )

    def _creates_cycle(self) -> bool:
        seen: set[int] = set()
        stack: list[int] = [self.parent_id]  # type: ignore
        while stack:
            node_id = stack.pop()
            if node_id == self.child_id:  # type: ignore
                return True
            if node_id in seen:
                continue
            seen.add(node_id)
            stack.extend(
                DefinitionLink.objects.filter(child_id=node_id).values_list(  # type: ignore
                    'parent_id', flat=True
                )
            )
        return False
