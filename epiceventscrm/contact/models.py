"""Contact model module"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models_config import POST_CHOICES


class Contact(AbstractUser):
    """Customisation of the User model"""
    post = models.CharField(
        max_length=20,
        choices=POST_CHOICES,
        default='ADMIN'
    )
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ', ' + self.last_name
