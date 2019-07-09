from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.validators import validate_email
from reviewer.models.reviewer import Reviewer


class ReviewerModelForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()

    class Meta:
        model = Reviewer
        fields = ['email', 'username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginModelForm(AuthenticationForm):
    username = UsernameField(
        max_length=128,
        validators=[validate_email, ]
    )
    password = forms.PasswordInput()
