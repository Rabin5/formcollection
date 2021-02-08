from users.models.user_group import GlobalPermission
from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model


CustomUser = get_user_model()


class UserGroupForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(), required=False)

    class Meta:
        model = Group
        fields = ['name', 'permissions', 'users']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "mobile_number", "groups")


class UserPermissionUpdateForm(forms.ModelForm):
    class Meta:
        model = GlobalPermission
        fields = ['name']
