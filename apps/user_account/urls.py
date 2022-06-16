from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from apps.user_account.views import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    # path('login/', LoginAPIView.as_view()),
    # path('logout/', LogoutAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("forgot_password/", ForgotPasswordView.as_view()),
    path('confirm_email/<str:activation_code>/', TakeNewPasswordView.as_view()),
]
