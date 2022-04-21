from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from eauth.models import UserProfile


class AdminProfile(UserAdmin):
    pass


admin.site.register(UserProfile, AdminProfile)