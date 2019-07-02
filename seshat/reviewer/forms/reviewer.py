from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.validators import validate_email
from reviewer.models.reviewer import Reviewer


class ReviewerModelForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Reviewer
        fields = ['email', 'username', 'password']


class LoginModelForm(AuthenticationForm):
    username = UsernameField(
        max_length=128,
        validators=[validate_email, ]
    )
    password = forms.PasswordInput()
