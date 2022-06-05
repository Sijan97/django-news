from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ Model definition for custom user create form. """
    class Meta(UserCreationForm):
        """ Overriding Meta class to add new custom field. """
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):
    """ Model definition for custom user change form. """
    class Meta(UserChangeForm):
        """ Overriding Meta class for custom user model """
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age')
