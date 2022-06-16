from django.db import models
from apps.product.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite')
    favorite = models.BooleanField(default=False)