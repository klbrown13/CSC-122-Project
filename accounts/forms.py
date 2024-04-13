from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ("email", "work_status", "job_type")
        fields = ("username","email", "work_status", "job_type")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserCreationForm.Meta.fields
        fields = ("username","email", "work_status", "job_type")
