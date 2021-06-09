from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Contact

class ContactCreationForm(UserCreationForm):

    class Meta:
        model = Contact
        fields = ('username', 'email', 'post', 'mobile')

class ContactChangeForm(UserChangeForm):

    class Meta:
        model = Contact
        fields = ('username', 'email', 'post', 'mobile')
