from django.db import models
from .team import Team

class Project(models.Model):
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