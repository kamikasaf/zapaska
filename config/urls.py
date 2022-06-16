
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter
from django.conf.urls.static import static
from django.conf import settings

from apps.favorite.views import FavoriteVIewSet
from apps.likes.views import LikesVIewSet
from apps.product.views import *
from apps.review.views import *
# from apps.order.views import OrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = SimpleRouter()
router.register('reviews', ReviewViewSet)
router.register('products', LikesVIewSet)
router.register('products', FavoriteVIewSet)
# router.register('order', OrderViewSet)




schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/', include('apps.user_account.urls')),
    
   #  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   #  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    path('category/', include('apps.category.urls')),
    path('products/', include('apps.product.urls')),
    path('', include(router.urls)),
    path('', include('apps.favorite.urls')),
    path('shoppingcart/', include('apps.cart.urls')),
    path('order/', include('apps.order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)