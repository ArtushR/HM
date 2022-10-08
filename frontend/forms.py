from users.admin import User
from .models import Product
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)

    class Meta:
        model = User
        fields = ["username", "password", "password2", "email"]
