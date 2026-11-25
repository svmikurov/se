from django.db import models


class Translation(models.Model):
    LENGTH = 100

    native = models.CharField(
        max_length=LENGTH,
    )
    foreign = models.CharField(max_length=LENGTH)
