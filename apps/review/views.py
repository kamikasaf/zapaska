from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from apps.product.permissions import IsAdminOrAuthor
from apps.review.models import Review
from apps.review.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
    def get_permissions(self):
        if self.action=='create':
            return [IsAuthenticated()]

        return [IsAdminOrAuthor()]

    def get_serializer_context(self):
        return {'request': self.request}