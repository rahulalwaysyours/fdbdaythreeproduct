from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom User model extending AbstractUser
class User(AbstractUser):
    # You can add additional fields here if needed
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Override default fields if necessary for custom behavior
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email'
    #username is from AbstractUser
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email