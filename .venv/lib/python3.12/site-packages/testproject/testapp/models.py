from django.db import models
from cuser.fields import CurrentUserField

class TestModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = CurrentUserField(
        add_only=True,
        blank=True,
        null=True,
        related_name="tests_created"
    )


class TestModel2(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()

