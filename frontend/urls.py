from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('profile/', views.about, name='profile'),

]


