from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "work_status",
        "job_type",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("work_status", "job_type")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("work_status", "job_type")}),)

admin.site.register(CustomUser, CustomUserAdmin)