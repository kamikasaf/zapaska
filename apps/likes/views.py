from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.serializers import ProductSerializer

from .models import Likes

class LikesVIewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['GET'])
    def like(self, request, pk):
        product = self.get_object()
        user = request.user
        like_obj, created = Likes.objects.get_or_create(product=product, user=user)
        if like_obj.is_liked == False:
            like_obj.is_liked = not like_obj.is_liked
            like_obj.save()
            return Response('you liked this product')
        else:
            like_obj.is_liked = not like_obj.is_liked
            like_obj.save()
            return Response('you disliked this product')

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action in ['like', 'favorite']:
            return [IsAuthenticated()]