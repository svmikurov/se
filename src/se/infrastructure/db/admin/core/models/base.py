"""Core abstract mixins for shared Django services.

This module defines small, orthogonal abstract mixins that concrete
models in individual services can compose:

- :class:`TimestampedMixin` — ``created_at`` / ``updated_at``.
- :class:`UserOwnedMixin` — ``user`` FK to ``AUTH_USER_MODEL``.
- :class:`AbstractUserOwnedModel` — convenience composition of both.

The mixins are independent on purpose: not every model needs a user, and
not every model needs timestamps. Services pick only what they need.
This module intentionally contains **no** concrete models, tables, or
migrations.

Design decisions
----------------

**Orthogonal mixins instead of one fat base.**
A single base model carrying ``user`` and timestamps would force every
subclass to accept both. Django fields cannot be cheaply removed or
re-tuned by a subclass, so a fat base leaks into models that never
needed those columns. Orthogonal mixins let each service compose exactly
the surface it needs. MRO composition order is left to the service; the
mixins declare no conflicting fields.

**Lazy reference to the user model.**
:class:`UserOwnedMixin.user` references ``settings.AUTH_USER_MODEL`` as
a string instead of calling ``get_user_model()`` at import time.
A shared core must not bind itself to a concrete user model: different
services may use different user models, and eager resolution introduces
circular-import risks (the user model may itself inherit from these
mixins). A string reference is resolved lazily by Django during app
loading.

**Templated ``related_name`` on the user FK.**
``related_name`` uses the ``%(app_label)s_%(class)s_set`` template.
Without it, Django would derive the reverse accessor from the abstract
mixin and every subclass would register the same name on the user model,
causing a conflict at check/migration time. Templating keeps each
subclass' reverse accessor unique automatically.

**Timestamp fields use ``auto_now_add`` / ``auto_now``.**
``created_at`` is set once on insert; ``updated_at`` refreshes on every
``save()``. This is the standard Django mechanism and requires no
boilerplate. Note that ``auto_now`` does not fire on
``QuerySet.update()`` — code that bypasses ``save()`` must set
``updated_at`` explicitly. The convenience is accepted deliberately;
callers who need strict accuracy can override the field.

**Lazy translations for ``verbose_name``.**
Field labels use ``gettext_lazy`` rather than ``gettext``.
``verbose_name`` is evaluated when forms, admin, and serializers are
built, not at import time; eager translation would freeze the message in
the language active during import and ignore the language of the actual
request.

**No concrete state in core.**
This module must not introduce concrete models, tables, or migrations.
Doing so would turn the core package into a shared database schema
between services, coupling their deployment and migration lifecycles and
turning a distributed system into a distributed monolith.
"""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedMixin(models.Model):
    """Adds ``created_at`` / ``updated_at`` to a concrete model."""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated'),
    )

    class Meta:
        abstract = True


class UserOwnedMixin(models.Model):
    """Adds a ``user`` FK to a concrete model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('User'),
    )

    class Meta:
        abstract = True


class AbstractUserOwnedModel(TimestampedMixin, UserOwnedMixin):
    """Convenience base for models owned by a user.

    Combines timestamps and user ownership. Adds no fields of its own.
    Additional fields, including ``name``, are the responsibility of the
    concrete model.
    """

    class Meta:
        abstract = True
