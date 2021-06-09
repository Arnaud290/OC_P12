from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Contact

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Contact
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Contact
        fields = ('email',)
