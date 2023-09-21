import datetime
import json
import math
import random
import time
import urllib.parse


from django.contrib.auth import update_session_auth_hash
from django.contrib.sessions.models import Session
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils import timezone
from rest_framework import generics, status, views, permissions, mixins
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from sendgrid import Content

# from .serializers import AppleSocialAuthSerializer, FacebookSocialAuthSerializer, RegisterSerializer, SetNewPasswordSerializer, ResetPasswordEmailRequestSerializer, \
#     EmailVerificationSerializer, LoginSerializer, LogoutSerializer, UserProfileSerializer, PasswordChangeSerializer, \
#     DeleteUserSerializer, ProfileSerializer

from .serializers import  RegisterSerializer , LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import User #, Profile

import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from django.http import HttpResponsePermanentRedirect, HttpResponse
import os
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
import logging



from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
# from .serializers import GoogleSocialAuthSerializer










from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from social_django.utils import psa

# from requests.exceptions import HTTPError
# http and https settings for email link
class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


'''Registering a new user and then sending a link to the 
 email for account activation . it includes encoding of the url as well. 
 It creates default location named Home for that user as well'''

logger = logging.getLogger(__name__)
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)
    

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        return Response(user_data, status=status.HTTP_201_CREATED)




# Log in api
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer

#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
        
#         try:
#             token_data = request.data['token_data']
#             st = Device.objects.get(token=token_data)
#             st.delete()
#             print("device deleted")
#         except:
#             print("device not found")
#         finally:
#             serializer = self.serializer_class(data=request.data)

#             serializer.is_valid(raise_exception=True)
#             serializer.save()
            
#             return Response(status=status.HTTP_204_NO_CONTENT)
