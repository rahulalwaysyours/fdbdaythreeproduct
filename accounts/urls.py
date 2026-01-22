from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import (
    UserRegistrationAPIView, 
    CustomTokenObtainView,
    verify_email,
    UserProfileAPIView,
    logout_view
)


urlpatterns = [
    # Authentication endpoints
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_view, name='logout'),
    
    # Email verification
    path('verify-email/', verify_email, name='verify-email'),
    
    # User profile
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]