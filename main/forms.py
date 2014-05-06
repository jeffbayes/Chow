from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

class RegisterNewUserForm(forms.Form):
    """ Form to create a new user/customer """
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password1 = forms.CharField(
        label="Password", 
        validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(50)],
        required=True,
        widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterNewUserForm, self).clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 or password2:
            if User.objects.filter(email=cleaned_data.get("email")).count():
                raise forms.ValidationError("Email address already registered")
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match")
        return cleaned_data
