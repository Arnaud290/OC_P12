from django.contrib import admin
from .models import Contract, Status


class StatusAdmin(admin.ModelAdmin):
   
    list_display = ['id', 'status_name']

admin.site.register(Contract)
admin.site.register(Status, StatusAdmin)
