from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('products/', views.products, name='products'),
    path("search/", SearchResultsView.as_view(), name="search"),
    path('about/', views.about, name='about'),
    path('profile/', views.about, name='profile'),
    path('register/', views.Register.as_view(), name='register'),

]


