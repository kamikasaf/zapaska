

from unicodedata import category
from .serializers import CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Category
from rest_framework.filters import OrderingFilter
import django_filters.rest_framework as filters
from rest_framework.response import Response
from rest_framework import status



class ListCategoryVIew(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )

    def get(self, request):
        search = request.query_params.get('search')
        if search:
            category = Category.objects.filter(title__icontains=search)
        else:
            category = Category.objects.order_by('title')

        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCategoryVIew(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, IsAuthenticated)



class DestroyCategoryVIew(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, )

class RetrieveCategoryVIew(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class UpdateCategoryVIew(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, )
