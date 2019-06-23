from django.db import models


class Service(models.Model):

    name = models.CharField(
        max_length=20
    )

    api = models.TextField()