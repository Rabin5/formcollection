from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'mobile_number', 'email', 'password', "groups")
        widgets = {
            'password': forms.PasswordInput(),
        }
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is already used please choose another one')
        return email
    def clean_mobile_number(self):
        mobile_number=self.cleaned_data.get('mobile_number')
        if not (len(mobile_number) == 10 and mobile_number.isdigit()):
            raise forms.ValidationError('mobile number is not valid')
        return mobile_number

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email", "mobile_number", "groups")


class ResetPasswordForm(SetPasswordForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    field_order = ['user', 'new_password1', 'new_password2']
