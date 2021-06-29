"""Admin page module"""
from django.contrib import admin
from .models import Client


class CustomClientAdmin(admin.ModelAdmin):
    model = Client

    list_filter = (
        'date_created',
        'date_updated',
        'status'
    )

    list_display = ['id', 'first_name', 'last_name', 'company_name', 'status']


admin.site.register(Client, CustomClientAdmin)
