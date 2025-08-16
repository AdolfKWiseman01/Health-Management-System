from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

# Add a filter for groups in the User admin
class CustomUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + ('groups',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Make sure the Group model is registered (it is by default)
admin.site.unregister(Group)
admin.site.register(Group)

