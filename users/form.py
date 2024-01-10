from django import forms
from .models import User


class UserSignUpForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Provide your full name",
            "class": "input-fields"
        }
    ), label="Full name")

    email = forms.EmailField(max_length=255, required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Provide your email",
            "class": "input-fields"
        }
    ), label="Email")
    phone_number = forms.CharField(max_length=10, required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Provide your phone number",
            "class": "input-fields"
        }
    ), label=" Phone Number")
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={
            "placeholder": "Provide your password",
            "class": "input-fields"
        }
    ), label="Password")
    # password = forms.PasswordInput()

    class Meta:
        model = User
        # fields = ['name', 'email', 'password']

        exclude = ['is_active', 'created_on', 'updated_on',]
