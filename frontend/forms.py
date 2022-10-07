from .models import Product
from django import forms
from django.forms import ModelForm, EmailInput, PasswordInput
from manager.models import Person

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
        model = Person
        fields = ["username", "password", "password2", "email"]

