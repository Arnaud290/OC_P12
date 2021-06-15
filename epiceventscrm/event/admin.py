from django.contrib import admin
from .models import Event, Status


class StatusAdmin(admin.ModelAdmin):
       
    list_display = ['id', 'status_name']

admin.site.register(Event)
admin.site.register(Status, StatusAdmin)