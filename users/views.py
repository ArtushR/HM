from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
