from rest_framework import serializers


from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework.exceptions import AuthenticationFailed


# to get the data of tables in the json formats

# user profile i.e. personal data



# creating a new user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(
        max_length=68, min_length=1)
    second_name = serializers.CharField(
        max_length=68, min_length=1)
    email = serializers.CharField(
        max_length=68, min_length=1)
    class Meta:
        model = User
        fields = ['email', 'password', 'second_name', 'first_name' ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        # display name check to make it unique
        us = User.objects.filter(email=email)
        if us.exists():
            raise ValidationError('Invalid credentials, try again')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    tokens = serializers.SerializerMethodField()
    

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access'],

        }

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise ValidationError('Account disabled, contact admin')
        
        return {
            'email': user.email,
            'tokens': user.tokens
        }

# Log out a user
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            if 'bad_token' in self.error_messages:
                raise serializers.ValidationError({
                    'refresh': [self.error_messages['bad_token']]
                })
            else:
                raise serializers.ValidationError({
                    'refresh': ['Token is expired or invalid']
                })

