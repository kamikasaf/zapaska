from django.urls import path
from .views import *


urlpatterns= [
    path('', OrderListVIew.as_view()),
    path('<int:pk>/', RetrieveOrderVIew.as_view()),
    path('create/', CreateOrderVIew.as_view()),
    path('delete/<int:pk>/', DestroyOrderVIew.as_view()),
    path('update/<int:pk>/', UpdateOrderVIew.as_view()),
]