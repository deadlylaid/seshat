from django.db import models
from django.conf import settings

from .repository import Repository


class Review(models.Model):
    STATUS_FIELDS = (
        ('OPEN', 'OPEN'),
        ('MERGED', 'MERGED'),
        ('DECLINED', 'DECLINED')
    )

    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=8, choices=STATUS_FIELDS)
    branch = models.CharField(max_length=150)
