from django.urls import path, re_path

from UserModule.serializers import FacebookSocialAuthSerializer
from .views import AppleSocialAuthView, ChangeEmailLink, CheckDuplicateView, FacebookSocialAuthView, GoogleSocialAuthView, PhoneOTPSendAPI, RegisterView, LogoutAPIView, SetNewPasswordAPIView, UserCodeAuthView, VerifyChangeEmail, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, \
    UserProfileView, RequestForgotPassword, UpdatePasswordView, ResendEmailLink, DeleteUserAccountView, ProfileView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from UserModule import views

# Api urls fro user module. Ctrl+click on the class name or visit views.py to view the class and detail comments
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),


]
