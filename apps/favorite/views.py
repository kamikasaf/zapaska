from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.favorite.serializers import FavoriteSerializer
from apps.product.models import Product
from apps.product.serializers import ProductSerializer

from .models import Favorite

class FavoriteVIewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['GET'])
    def favorite(self, request, pk):
        product = self.get_object()
        user = request.user
        like_obj, created = Favorite.objects.get_or_create(product=product, user=user)
        if like_obj.favorite == False:
            like_obj.favorite = not like_obj.favorite
            like_obj.save()
            return Response('you added this product to favorite')
        else:
            like_obj.favorite = not like_obj.favorite
            like_obj.save()
            return Response('you deleted this product from favorite')

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action in ['like', 'favorite']:
            return [IsAuthenticated()]


class FavoriteView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = super().get_queryset() 
        queryset = queryset.filter(favorite__user=self.request.user, favorite__favorite=True)
        return queryset