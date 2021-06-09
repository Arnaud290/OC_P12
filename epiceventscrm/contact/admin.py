from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Contact


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Contact
    list_display = (
        'username',
        'email',
        'is_active',
        'post',
        'mobile'
    )
    list_filter = (
        'username',
        'email',
        'is_active',
        'post',
        'mobile'
    )
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password', 'post')}
        ),
        (
            'Permissions',
            {'fields': ('is_superuser', 'is_active')}
        ),
    )
    add_fieldsets = (
        (None, 
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
