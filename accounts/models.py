from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Model definition for custom user. """
    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):
    """ Model definition for managing user profile. """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="user.jpg", upload_to="images/")

    def __str__(self):
        return f"{ self.user.username } Profile"
