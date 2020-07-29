from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    # Email as unique user identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        if not self.first_name:
            return self.email
        return super().get_short_name()

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return self.email
        return super().get_full_name()

    def __str__(self):
        return self.email
