from django.contrib.auth.models import AbstractUser
from django.db import models
from .models_config import POST_CHOICES


class Contact(AbstractUser):
    post = models.CharField(
        max_length=20,
        choices=POST_CHOICES
    )
    mobile = models.CharField(max_length=20)

    def __str__(self):
        contact = self.first_name + ' ' +\
            self.last_name + ' ' + self.email
        return contact
