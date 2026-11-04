"""Term form."""

from typing import Any, TypeVar

from django import forms
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
    explanation_text = forms.CharField(
        label=_('Explanation'),
        max_length=Explanation.EXPLANATION_MAX_LENGTH,
        widget=forms.Textarea,
    )
    owner: Any | None = None

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
            self.fields['user'].initial = self.owner
            self.fields[
                'definition_text'
            ].initial = self.instance.definition.text
            self.fields[
                'explanation_text'
            ].initial = self.instance.explanation.text

    def clean(self) -> dict[str, Any]:
        cleaned: dict[str, Any] = super().clean() or {}
        if self.owner is None:
            raise forms.ValidationError('Owner is required to create a term.')
        return cleaned

    def _get_or_create(self, model: type[M], text: str) -> M:
        try:
            with transaction.atomic():
                obj, _ = model.objects.get_or_create(  # type: ignore[attr-defined]
                    user=self.owner,
                    text=text,
                )
            return obj  # type: ignore[no-any-return]
        except IntegrityError:
            # Concurrent create: another request inserted the same row.
            return model.objects.get(user=self.owner, text=text)  # type: ignore[attr-defined, no-any-return]

    @transaction.atomic
    def save(self, commit: bool = True) -> Term:
        term: Term = super().save(commit=False)
        term.user = self.owner
        term.definition = self._get_or_create(
            Definition,
            self.cleaned_data['definition_text'],
        )
        term.explanation = self._get_or_create(
            Explanation,
            self.cleaned_data['explanation_text'],
        )
        if commit:
            term.save()
            self.save_m2m()
        return term
