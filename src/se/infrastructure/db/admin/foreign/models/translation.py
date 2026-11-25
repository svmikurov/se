from django.db import models

from ...core.models import AbstractUserOwnedModel


class Translation(AbstractUserOwnedModel):
    LENGTH = 100

    native = models.CharField(
        max_length=LENGTH,
    )
    foreign = models.CharField(
        max_length=LENGTH,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'native', 'foreign'],
                name='%(app_label)s_%(class)s_user_native_foreign_uniq',
            ),
        ]
