from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User
from accounts.serializers import UserRegistrationSerializer, UserSerializer
from accounts.utils import send_verification_email

# Create your views here.

#API view for user registration using generics.CreateAPIView and the UserRegistrationSerializer
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()

    # Use the UserRegistrationSerializer for handling user registration
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        emaiil_sent = send_verification_email(user)

        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully. Please check your email to verify your account.',
            'email_sent': emaiil_sent
        }, status=status.HTTP_201_CREATED
        )

#API view for user registration will be created in accounts/urls.py using the serializer
#login view using JWT tokens
#LOGIN API view
class CustomTokenObtainView(TokenObtainPairView):
    # You can customize the serializer if needed
    pass