from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView

from users.forms.user_group_forms import UserGroupForm, UserPermissionUpdateForm
from users.models.user_group import GlobalPermission
from users.models.user import User

class CreateGroup(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView, SuccessMessageMixin):
    model = Group
    form_class = UserGroupForm
    template_name = 'user_groups/add_group.html'
    # success_message = 'Successfully created.'
    permission_required = 'users.perm_user_management'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permissions'] = GlobalPermission.objects.filter(content_type__model='global permission').order_by(
            'name')
        context['users'] = User.objects.all().order_by('username')
        return context

    def form_valid(self, form):
        group = form.save()
        users = form.cleaned_data.get('users')
        group.user_set.add(*users)
        return super(CreateGroup, self).form_valid(form)


    def get_success_url(self) -> str:
        return reverse_lazy('users:groups_list')


class ListGroup(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'user_groups/list_groups.html'
    permission_required = 'users.perm_user_management'

    def get(self, request, **kwargs):
        context = {}
        context['query'] = request.GET.get('query', '')
        context['permissions'] = GlobalPermission.objects.filter(content_type__model='global permission').order_by(
            'name')
        
        # users = User.objects.for_user(request.user).order_by('email')
        # if context['query']:
        #     users = users.filter(username__contains=context['query'])
        
        # user_paginator = Paginator(users, 20)
        # user_page_num = request.GET.get('page')
        # context['users'] = user_paginator.get_page(user_page_num)

        context['groups'] = Group.objects.all().order_by('name')
        return render(request, self.template_name, context=context)

    


class GroupDetail(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Group
    template_name = 'user_groups/group_detail.html'
    context_object_name = 'group'
    permission_required = 'users.perm_user_management'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_active=True)
        # context['users'] = User.objects.filter(is_active=True)
        # context['users'] = User.objects.filter(self.request.user,
        #     is_active=True).exclude(groups=self.object)
        context['group_permissions'] = self.object.permissions.all()
        context['permissions'] = GlobalPermission.objects.filter(
            content_type__model='global permission').exclude(id__in=context['group_permissions'])

        return context


# @permission_required('user_groups.roles_mgmt_permission', raise_exception=True)
# def search_users_in_group_detail(request):
#     q = request.GET.get('q')
#     if q:
#         users = User.objects.filter(profile__full_name__icontains=q)[:10]
#     else:
#         users = User.objects.filter(is_active=True).order_by('profile__full_name')[:10]

#     return render(request, 'user_groups/users_in_group_detail.html', {'users': users})


# @permission_required('user_groups.roles_mgmt_permission', raise_exception=True)
# def assign_users_in_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     users = request.POST.getlist('users')
#     if users:
#         for i in users:
#             user = get_object_or_404(User, pk=i)
#             if user in group.user_set.all():
#                 group.user_set.remove(user)
#             group.user_set.add(user)
#         messages.success(request, 'Successfully done.')
#         return redirect('users:group_detail', group.pk)


class RemoveUserFromGroup(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = 'user_management.perm_user_management'
    permission_required = 'users.perm_user_management'

    def post(self, request, **kwargs):
        group = get_object_or_404(Group, pk=kwargs['pk'])
        user = get_object_or_404(User, pk=kwargs['user_pk'])
        group.user_set.remove(user)
        if group.name == 'ROLE_MODERATOR':
            user.is_moderator = False
            user.save()
        # UserActivity.objects.create(user=request.user.username,
        #                             change_message='Users removed from group "{}"'.format(group.name))
        messages.success(request, 'Successfully done.')
        return redirect('users:group_detail', group.pk)

class RemovePermissionFromGroup(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = 'user_management.perm_user_management'
    permission_required = 'users.perm_user_management'

    def post(self, request, **kwargs):
        group = get_object_or_404(Group, pk=kwargs['pk'])
        permission = get_object_or_404(GlobalPermission, pk=kwargs['perm_pk'])
        group.permissions.remove(permission)
        # UserActivity.objects.create(user=request.user.username,
        #                             change_message='Permissions removed from group "{}"'.format(group.name))
        messages.success(request, 'Successfully done.')
        return redirect('users:group_detail', group.pk)

class AssignUserInGroup(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = 'user_management.perm_user_management'
    permission_required = 'users.perm_user_management'

    def post(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=kwargs['pk'])
        users = request.POST.getlist('users')
        pks = [User.objects.get(pk=user) for user in users]
        users = User.objects.filter(pk__in=users)
        if pks:
            group.user_set.add(*pks)
            if group.name == 'ROLE_MODERATOR':
                users.update(is_moderator=True)
            # UserActivity.objects.create(
            #     user=request.user.username, change_message='Users assigned in group "{}"'.format(group.name))
            messages.success(request, 'Successfully done.')
            return redirect('users:group_detail', group.pk)
        else:
            return redirect('users:group_detail', group.pk)

class AssignPermissionInGroup(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = 'user_management.perm_user_management'
    permission_required = 'users.perm_user_management'

    def post(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=kwargs['pk'])
        permissions = request.POST.getlist('permissions')
        print(permissions)
        pks = [GlobalPermission.objects.get(
            pk=permission) for permission in permissions]
        if pks:
            group.permissions.add(*pks)
            # UserActivity.objects.create(
            #     user=request.user.email, change_message='Permissions assigned in group "{}"'.format(group.name))
            return redirect('users:group_detail', group.pk)
        else:
            return redirect('users:group_detail', group.pk)

class ChangeGroupName(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = 'user_management.perm_user_management_stray'
    permission_required = 'users.perm_user_management'

    def post(self, request, **kwargs):
        group = get_object_or_404(Group, pk=kwargs['pk'])
        name = request.POST.get('name')
        Group.objects.filter(pk=group.pk).update(name=name)
        # UserActivity.objects.create(
        #     user=request.user.username, change_message='Group name changed to "{}"'.format(group.name))
        return redirect('users:group_detail', group.pk)



class UpdateGroup(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView, SuccessMessageMixin):
    model = Group
    form_class = UserGroupForm
    template_name = 'user_groups/update_group.html'
    # success_message = 'Successfully updated.'
    context_object_name = 'group'
    permission_required = 'user_groups.roles_mgmt_permission'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permissions'] = GlobalPermission.objects.filter(content_type__model='global permission').order_by(
            'name')
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('users:groups_list')


class DeleteGroup(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Group
    template_name = 'user_groups/delete_group.html'
    context_object_name = 'group'
    permission_required = 'user_groups.roles_mgmt_permission'

    def get_success_url(self) -> str:
        return reverse_lazy('users:groups_list')

# # @permission_required('user_groups.roles_mgmt_permission', raise_exception=True)
# def delete_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'POST':
#         group.delete()
#         messages.success(request, 'Successfully deleted.')
#         return redirect('users:list_groups')

class CreatePermissionView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = GlobalPermission
    fields = ['name', 'codename']
    template_name = 'user_groups/create_permission.html'
    success_url = reverse_lazy('users:list_permissions')
    permission_required = 'users.perm_user_management'

    def test_func(self):
        return self.request.user.is_superuser



class ListPermissionView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = GlobalPermission
    context_object_name = 'permissions'
    template_name = 'user_groups/list_permissions.html'
    permission_required = 'user_management.perm_user_management'

    def get_queryset(self):
        return GlobalPermission.objects.filter(content_type__model='global permission').order_by('name')


class EditPermissionView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.perm_user_management'
    model = GlobalPermission
    template_name = "user_groups/permission_update.html"
    form_class = UserPermissionUpdateForm
    success_url = reverse_lazy('users:list_permissions')
    context_object_name = 'permission'

class DeletePermission(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = GlobalPermission
    context_object_name = 'permission'
    # success_url = reverse_lazy('user_management.perm_user_management')
    template_name = 'user_groups/delete_permissions.html'
    permission_required = 'users.perm_user_management'

    def test_func(self) -> None:
        return self.request.user.is_superuser

