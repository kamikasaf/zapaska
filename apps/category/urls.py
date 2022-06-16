from django.urls import path
from .views import *


urlpatterns = [
    path('', ListCategoryVIew.as_view()),
    path('<int:pk>/', RetrieveCategoryVIew.as_view()),
    path('create/', CreateCategoryVIew.as_view()),
    path('delete/<int:pk>/', DestroyCategoryVIew.as_view()),
    path('update/<int:pk>/', UpdateCategoryVIew.as_view())
]