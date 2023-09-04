from django.contrib import admin

# Register your models here.
from .models import User

"""First, the code imports the necessary components from the Django framework, specifically the admin module.

Then, it imports the User and Profile models from the app's models file using a relative import syntax.

Next, it defines a UserAdmin class that inherits from the admin.ModelAdmin class. This class contains a list_display 
attribute, which specifies the fields to be displayed in the admin view for the User model.

Similarly, an InstallerAdmin class is defined, which specifies the fields to be displayed for the Profile model.

Finally, the code registers both models with their respective admin classes using the admin.site.register() method. 
This makes the views defined by UserAdmin and InstallerAdmin available in the admin interface of the Django app."""


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)
