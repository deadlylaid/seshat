from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Email is required')

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Reviewer(AbstractBaseUser):
    objects = CustomUserManager()

    email = models.EmailField(
        max_length=100,
        unique=True,
    )

    username = models.CharField(
        max_length=30,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']