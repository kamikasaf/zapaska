from django.db import models

from apps.product.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()


class Likes(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)