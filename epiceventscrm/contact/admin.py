from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ContactCreationForm, ContactChangeForm
from .models import Contact


class ContactAdmin(UserAdmin):
    add_form = ContactCreationForm
    form = ContactChangeForm
    model = Contact
    list_display = ['email', 'username',]

admin.site.register(Contact, ContactAdmin)
