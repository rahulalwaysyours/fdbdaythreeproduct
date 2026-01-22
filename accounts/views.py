from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import User
from accounts.serializers import UserRegistrationSerializer, UserSerializer, CustomTokenObtainPairSerializer
from accounts.utils import send_verification_email

# Create your views here.

#API view for user registration using generics.CreateAPIView and the UserRegistrationSerializer
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    # Use the UserRegistrationSerializer for handling user registration
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        email_sent = send_verification_email(user)

        return Response({
            'user': UserSerializer(user).data,
            'message': 'User registered successfully. Please check your email to verify your account.',
            'email_sent': email_sent
        }, status=status.HTTP_201_CREATED)


#Custom JWT login view with email verification check
class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]


# Email verification endpoint
@api_view(['GET'])
def verify_email(request):
    token = request.query_params.get('token')
    
    if not token:
        return Response(
            {'error': 'Verification token is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = User.objects.get(email_verification_token=token)
        
        if user.email_verified:
            return Response(
                {'message': 'Email already verified.'},
                status=status.HTTP_200_OK
            )
        
        user.email_verified = True
        user.email_verification_token = None
        user.save()
        
        return Response(
            {'message': 'Email verified successfully. You can now login.'},
            status=status.HTTP_200_OK
        )
    except User.DoesNotExist:
        return Response(
            {'error': 'Invalid verification token.'},
            status=status.HTTP_400_BAD_REQUEST
        )


# User profile endpoint
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# Logout endpoint - invalidate tokens
@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data.get("refresh_token")
        
        if not refresh_token:
            return Response(
                {"error": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        token = RefreshToken(refresh_token)
        token.blacklist()
        
        return Response(
            {"message": "Successfully logged out."},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )