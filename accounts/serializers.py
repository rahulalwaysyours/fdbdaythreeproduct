from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import User

#for registering new user
class UserRegistrationSerializer(serializers.ModelSerializer):
    #password field should be write only and not be returned in responses
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password,])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    #attrs gives you JSON data sent by user
    def validate(self, attrs):
        if(attrs['password'] != attrs['password2']):
            #if passwords do not match, raise error in JSON format too
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    #when creating user, we need to hash the password
    def create(self, validated_data):
        validated_data.pop('password2')  #remove password2 as it's not needed for user creation
        #keyword arguments unpacking to pass remaining fields
        user = User.objects.create_user(**validated_data) #create_user method hashes the password
        # user.save() # No need to call save() again as create_user already saves the user
        return user


    class Meta:
        model = User  # Assuming User model is imported
        fields = (
            'username',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number'
       )
        extra_kwargs = {
            'password': {'write_only': True},
        }


#for displaying user details
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User # Assuming User model is imported
        #first_name and last_name are from AbstractUser
        fields = (
            'username',
            'id',
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'date_joined',
            #'phone_number', we are not including here because it will be then verified through OTP
            'email_verified',
        )

# Custom JWT token serializer to include additional user info
# TokenObtainPairSerializer is from rest_framework_simplejwt that will be null if validation fails
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs) # Call the original validate method
        user = self.user

        if not user or user.email_verified == False:
            raise AuthenticationFailed('No active account found with the given credentials')
        
        return data
    
    @classmethod # class method to customize token payload
    def get_token(clas, user):
        token = super().get_token(user) # Get the original token

        # Add custom claims
        token['username'] = user.username 
        token['email'] = user.email
        token['email_verified'] = user.email_verified

        return token