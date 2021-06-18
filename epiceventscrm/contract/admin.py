"""Admin page module"""
from django.contrib import admin
from .models import Contract, Status


class CustomContractAdmin(admin.ModelAdmin):
    model = Contract

    list_filter = (
        'date_created',
        'date_updated',
        'status_id__status_name'
    )


class CustomStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']


admin.site.register(Contract, CustomContractAdmin)
admin.site.register(Status, CustomStatusAdmin)
