from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': "text",
                   'id': "inputLogin",
                   'class': 'form-control',
                   'required': 'required',
                   'autofocus': 'autofocus'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': "password", 'id': "inputPassword", 'class': 'form-control', 'autofocus': 'autofocus'}
        )
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': "text", 'id': "inputLogin", 'class': 'form-control', 'autofocus': 'autofocus'}
        )
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'type': "password", 'id': "inputPassword", 'class': 'form-control', 'required': 'required'}
        )
    )
    password2 = forms.CharField(required=False)
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': "text", 'id': "inputLogin", 'class': 'form-control'}
        )
    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': "text", 'id': "inputLogin", 'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'password1')
