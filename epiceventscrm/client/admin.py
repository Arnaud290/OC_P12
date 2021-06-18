"""Admin page module"""
from django.contrib import admin
from .models import Client


class CustomClientAdmin(admin.ModelAdmin):
    model = Client

    list_filter = (
        'date_created',
        'date_updated',
    )


admin.site.register(Client, CustomClientAdmin)
