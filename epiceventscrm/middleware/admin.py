"""Admin page module"""
from django.contrib import admin
from .models import ContactLog


class CustomContactLogAdmin(admin.ModelAdmin):
    model = ContactLog
    list_filter = ['method', 'date']
    list_display = ['id', 'date', 'username', 'method', 'request_url']
    actions = None

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(ContactLog, CustomContactLogAdmin)
