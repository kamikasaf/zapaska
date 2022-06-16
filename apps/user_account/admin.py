from django.contrib import admin

from apps.user_account.models import CustomUser

admin.site.register(CustomUser)