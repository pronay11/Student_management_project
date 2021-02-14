from django.contrib import admin
from .models import Staffs

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from student_management_system_app.models import Custom


class UserModel(UserAdmin):
    pass


admin.site.register(Custom, UserModel)
admin.site.register(Staffs)
