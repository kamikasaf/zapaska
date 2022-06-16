from apps.cart.models import ShoppingCart

def post_screate_cart_signal(sender, instance, created, *args, **kwargs):
    if created:
        ShoppingCart.objects.create(author=instance)
        