"""Term form."""

from typing import Any, TypeVar

from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.db import IntegrityError, transaction
from django.db.models import Model
from django.utils.translation import gettext as _

from ..models import Definition, Explanation, Term

M = TypeVar('M', bound=Model)


class TermForm(forms.ModelForm):  # type: ignore[type-arg]
    """Create or edit a Term."""

    definition_text = forms.CharField(
        label=_('Definition'),
        max_length=Definition.DEFINITION_MAX_LENGTH,
    )
    abbreviation_text = forms.CharField(
        label=_('Abbreviation'),
        max_length=Definition.ABBREVIATION_MAX_LENGTH,
        required=False,
    )
    translation_text = forms.CharField(
        label=_('Translation'),
        max_length=Definition.DEFINITION_MAX_LENGTH,
        required=False,
    )
    explanation_text = forms.CharField(
        label=_('Explanation'),
        max_length=Explanation.EXPLANATION_MAX_LENGTH,
        widget=forms.Textarea,
        required=False,
    )

    owner: AbstractBaseUser | None = None

    class Meta:
        model = Term
        fields: tuple[str, ...] = ()

    def __init__(
        self,
        *args: Any,
        owner: Any | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.owner = owner or (
            self.instance.user if self.instance.pk else None
        )
        if self.instance and self.instance.pk:
            definition = self.instance.definition
            self.fields['definition_text'].initial = definition.text
            self.fields['abbreviation_text'].initial = definition.abbreviation
            self.fields['translation_text'].initial = definition.translation
            self.fields[
                'explanation_text'
            ].initial = self.instance.explanation.text

    def clean(self) -> dict[str, Any]:
        cleaned = super().clean() or {}
        if self.owner is None:
            raise forms.ValidationError(
                _('Owner is required to create a term.'),
            )
        return cleaned

    def _get_or_create_definition(
        self,
        text: str,
        abbreviation: str,
        translation: str,
    ) -> Definition:
        try:
            with transaction.atomic():
                obj, _created = Definition.objects.get_or_create(  # type: ignore[attr-defined]
                    user=self.owner,
                    text=text,
                    defaults={
                        'abbreviation': abbreviation,
                        'translation': translation,
                    },
                )
            return obj  # type: ignore[no-any-return]
        except IntegrityError:
            return Definition.objects.get(user=self.owner, text=text)  # type: ignore[attr-defined, no-any-return]

    def _get_or_create_explanation(self, text: str) -> Explanation:
        try:
            with transaction.atomic():
                obj, _created = Explanation.objects.get_or_create(  # type: ignore[attr-defined]
                    user=self.owner,
                    text=text,
                )
            return obj  # type: ignore[no-any-return]
        except IntegrityError:
            return Explanation.objects.get(user=self.owner, text=text)  # type: ignore[attr-defined, no-any-return]

    @transaction.atomic
    def save(self, commit: bool = True) -> Term:
        term: Term = super().save(commit=False)
        term.user = self.owner
        term.definition = self._get_or_create_definition(
            text=self.cleaned_data['definition_text'],
            abbreviation=self.cleaned_data['abbreviation_text'],
            translation=self.cleaned_data['translation_text'],
        )
        term.explanation = self._get_or_create_explanation(
            text=self.cleaned_data['explanation_text'],
        )
        if commit:
            term.save()
        return term
