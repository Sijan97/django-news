from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Model definition for custom user. """
    age = models.PositiveIntegerField(null=True, blank=True)
