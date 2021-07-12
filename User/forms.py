
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError("Username already present.Please change username")

        except User.DoesNotExist:


            if username and email and password and confirm and password !=confirm:
                raise forms.ValidationError("Please you check your information")

            values ={
            'username':username,
            'email': email,
            'password':password
           }
            return values

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
