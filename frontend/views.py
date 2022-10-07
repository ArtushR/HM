from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from users.views import *


def products(request):
    products = Product.objects.all()
    for pr in products:
        pr.image = f'http://127.0.0.1:8000/media/{pr.image}'

    return render(request, 'products.html', {'products': products})


def about(request):
    return render(request, 'about.html', {'about': about})


def profile(request):
    return render(request, 'userpage.html', {'profile': profile})


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class SearchResultsView(ListView):
    model = Product
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(productname__icontains=query) | Q(description__icontains=query)
        )
        return object_list
