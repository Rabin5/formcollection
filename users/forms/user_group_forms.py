from django import forms
from django.contrib.auth.models import Group, Permission


class UserGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
