# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken



# User manager contains the function to create a user and also
# a superuser that creates an admin which can log in to the admin site
class UserManager(BaseUserManager):
    # create normal user
    def create_user(self, email,  password=None):

        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        
        user.save()
        return user

    def create_installer_user(self, email,  password=None):

        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        
        user.save()
        return user

    # create superuser
    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email,  password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

# Right now only email is being used as auth provider . but in future we can use the rest
# of the apps as well as  facebook , google ,twitter  e.t.c.
AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


# User table
class User(AbstractBaseUser, PermissionsMixin):
    # Types of the users on the basis of charger usage and account deleted
    class UserTypeChoices(models.TextChoices):
        BASIC = 'BASIC',
        COMMERCIAL = 'COMMERCIAL',
        BASIC_DELETED = 'BASIC_DELETED',
        COMMERCIAL_DELETED = 'COMMERCIAL_DELETED'

    # Types of the user i.e.  customer or both
    class UserProfileTypeChoices(models.TextChoices):
        CUSTOMER = 'CUSTOMER',
        INSTALLER = 'INSTALLER',
        BOTH = 'BOTH'

    email = models.EmailField(max_length=255,blank=True, unique=True, db_index=True)
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is banned is for future if it wants to ban a customer or installer
    is_banned = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'  # log in field
    

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

