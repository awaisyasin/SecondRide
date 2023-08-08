from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=100)
    phone = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    # password = forms.CharField(widget=forms.PasswordInput)

class CustomAuthenticationForm(AuthenticationForm):
    # username = forms.CharField(max_length=100)
    phone = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    # password = forms.CharField(widget=forms.PasswordInput)
