from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.user_products, name="products"),
]