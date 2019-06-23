from django.db import models
from reviewer.models import Reviewer


class Team(models.Model):
    name = models.CharField(
        max_length=20,
    )


class TeamMember(models.Model):
    user = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
