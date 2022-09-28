from django.shortcuts import render
from .models import *

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
def about(request):
    return render(request, 'about.html', {'about': about})
def profile(request):
    return render(request, 'userpage.html', {'profile': profile})