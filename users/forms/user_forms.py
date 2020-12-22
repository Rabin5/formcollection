from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'mobile_number', 'email', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'mobile_number', 'email',)


class ResetPasswordForm(SetPasswordForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    field_order = ['user', 'new_password1', 'new_password2']
