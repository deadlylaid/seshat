from django.db import models
from .team import Team


class Repository(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=30,
    )

    # using in api urls
    nickname = models.CharField(
        max_length=30,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
