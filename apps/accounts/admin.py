from django.contrib import admin
from apps.accounts.models import Employee, CustomUser

# Register your models here.
admin.site.register([CustomUser,Employee])
