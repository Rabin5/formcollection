from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView

from users.forms.user_forms import UserCreateForm, UserUpdateForm, ResetPasswordForm

User = get_user_model()


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    permission_required = ''
    form_class = UserCreateForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('md-users:list')


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = ''
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    permission_required = ''
    template_name = "users/user_update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('md-users:list')
    context_object_name = 'user'


class ResetPasswordView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = ResetPasswordForm
    permission_required = ''
    success_url = reverse_lazy('md-users:list')
    template_name = 'users/reset_password.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.POST:
            user_id = self.request.POST.get('user')
            user = get_object_or_404(User, pk=user_id)
            kwargs['user'] = user
        else:
            kwargs['user'] = None
        return kwargs
    
    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class ChangePasswordView(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('md-users:list')