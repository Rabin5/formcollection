from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.views.generic.base import View
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group

from users.forms.user_forms import UserCreateForm, UserUpdateForm, ResetPasswordForm

User = get_user_model()


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    permission_required = 'users.perm_user_management'
    form_class = UserCreateForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('users:list')


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.perm_user_management'
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    permission_required = 'users.perm_user_management'
    template_name = "users/user_update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:list')
    context_object_name = 'user'
    # success_message = "सफलतापूर्वक प्रयोगकर्ता विवरण अपडेट गरियो।"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()

        return context


class ResetPasswordView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # form_class = ResetPasswordForm
    permission_required = 'users.perm_user_management'
    success_url = reverse_lazy('users:list')
    template_name = 'users/reset_password.html'

    def get(self, request, pk, username, **kwargs):
        if pk:
            user = get_object_or_404(
                User,
                pk=pk
            )
            context = {
                'user': user,
            }
            print(context)
            return render(request, self.template_name, context=context)
        
        return redirect('users:list')

    def post(self, request, pk, username, **kwargs):
        if pk:
            user = get_object_or_404(
                User,
                pk=pk,
            )
            password = request.POST.get('password')
            password1 = request.POST.get('password1')

            if password != password1:
                messages.error(request, 'प्रविष्ट पासवर्डहरू मेल खाँदैन।')
                context = {
                    'user': user,
                }

                return render(request, self.template_name, context=context)
            else:
                user.set_password(password)
                user.save()
                messages.success(request, f'{user.username}को पासवर्ड परिवर्तन भयो ।')
                return HttpResponseRedirect(reverse('users:list'))



    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     if self.request.POST:
    #         user_id = self.request.POST.get('user')
    #         user = get_object_or_404(User, pk=user_id)
    #         kwargs['user'] = user
    #     else:
    #         kwargs['user'] = None
    #     return kwargs
    
    # def form_valid(self, form):
    #     form.save()
    #     # Updating the password logs out all other sessions for the user
    #     # except the current one.
    #     update_session_auth_hash(self.request, form.user)
    #     return super().form_valid(form)


class ChangePasswordView(LoginRequiredMixin, PermissionRequiredMixin, PasswordChangeView):
    permission_required = 'users.perm_user_management'
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:list')