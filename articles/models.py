from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings


class Article(models.Model):
    """ Model definition for newspaper articles. """
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="images/", null=True, blank=True)

    # String representation of model for admin view
    def __str__(self):
        return self.title

    # Defining function to get absolute url
    def get_absolute_url(self):
        return reverse("article_list", args=[str(self.id)])
