from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Contact


class CustomUserAdmin(UserAdmin):
    model = Contact
    list_display = (
        'username',
        'email',
        'is_active',
        'post',
        'mobile',
        'last_login'
    )
    list_filter = (
        'is_active',
        'post',
        'is_superuser',
        'last_login'
    )
    fieldsets = (
        (
            'Profil',
            {
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'mobile',
                    'password',
                    'post'
                )
            }
        ),
        (
            'Permissions',
            {'fields': ('is_superuser', 'is_active')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                    'is_superuser',
                    'is_active',
                    'post',
                    'mobile'
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Contact, CustomUserAdmin)
admin.site.unregister(Group)
