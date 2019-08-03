from django.db import models


class Repository(models.Model):
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
