"""Middleware Models Module"""
from django.db import models


class ContactLog(models.Model):
    username = models.CharField(max_length=255)
    method = models.CharField(max_length=20)
    request_url = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
