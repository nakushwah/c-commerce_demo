from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
            'contact',
            'contact2',
            'password1',
            'password2',

        ]
