from django.db import models


class Definition(models.Model):
    MAX_LENGTH = 40

    name = models.CharField(max_length=MAX_LENGTH)
