"""Admin page module"""
from django.contrib import admin
from .models import Event, Status


class CustomEventAdmin(admin.ModelAdmin):
    model = Event

    list_filter = (
        'date_created',
        'date_updated',
        'status_id__status_name'
    )
    list_display = ['id', 'date_created', 'client_id', 'status_id']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']


admin.site.register(Event, CustomEventAdmin)
admin.site.register(Status, StatusAdmin)
