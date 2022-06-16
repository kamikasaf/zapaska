from django.urls import path

from apps.cart.views import *

urlpatterns = [
    path('', ShoppingCartView.as_view()),
    path('<int:pk>/', ShoppingCartView.as_view()),
    path('delete/<int:pk>/', ShoppingCartView.as_view()),
    path('put/<int:pk>/', ShoppingCartView.as_view()),
    path('add/', AddProductInCartView.as_view()),
]