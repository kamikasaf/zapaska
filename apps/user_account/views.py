
from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema 



# from .services.utils import confirm_email
from .serializers import *

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

# class LoginAPIView(TokenObtainPairView):
#     serializer_class = LoginSerializer
    # def post(self,request):
    #     data = request.POST
    #     serializer = UserSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         user = serializer.validated_data.get('user')
    #         token, object = Token.objects.get_or_create(user=user)
    #         return Response({'Token': token.key})


# class LogoutAPIView(APIView):

#     def get(self, request):
#         user = request.user
#         token = Token.objects.get(user=user)
#         token.delete()  
#         return HttpResponse('goodbye', status=status.HTTP_401_UNAUTHORIZED)

class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            You are done!
            Please, confirm your email
            """
            return Response(message)

class ActivationView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active=True
        user.activation_code=''
        user.save()
        return Response('Your account is successfully activated!')


class ForgotPasswordView(APIView):
    @swagger_auto_schema(request_body=ForgotSerializer)
    def post(self, request):
        data = request.POST
        serializer = ForgotSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            confirm your email
            """
            return Response(message)

class TakeNewPasswordView(APIView):
    
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        new_password=user.password = user.generate_activation_code()
        user.set_password(new_password)
        user.save()
        return Response(f'Your new password: {new_password}')