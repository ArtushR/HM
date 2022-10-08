from django.urls import path
from . import views
from .views import SearchResultsView, ProductDetailView, products

urlpatterns = [
    path('products/', views.products, name='products'),
    path("search/", SearchResultsView.as_view(), name="search"),
    path('about/', views.about, name='about'),
    path('profile/', views.about, name='profile'),
    path('register/', views.Register.as_view(), name='register'),
    #path('products/{{ productname }}/', views.ProdDetailView.as_view(), name='product_detail'),
    #path('products/product_detail/', views.ProdDetailView.as_view(), name='product_detail'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]


