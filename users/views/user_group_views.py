from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from users.forms.user_group_forms import UserGroupForm
from users.models.user_group import GlobalPermission
from users.models.user import User

class CreateGroup(PermissionRequiredMixin, generic.CreateView, SuccessMessageMixin):
    model = Group
    form_class = UserGroupForm
    template_name = 'user_groups/add_group.html'
    success_message = 'Successfully created.'
    # permission_required = 'user_groups.roles_mgmt_permission'
    permission_required = ''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permissions'] = GlobalPermission.objects.filter(content_type__model='global permission').order_by(
            'name')
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('md-users:groups_list')


class ListGroup(PermissionRequiredMixin, generic.ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'user_groups/list_groups.html'
    # permission_required = 'user_groups.roles_mgmt_permission'
    permission_required = ''


# class GroupDetail(PermissionRequiredMixin, generic.DetailView):
#     model = Group
#     template_name = 'user_groups/group_detail.html'
#     context_object_name = 'group'
#     permission_required = 'user_groups.roles_mgmt_permission'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = User.objects.filter(is_active=True).order_by('profile__full_name')[:10]
#         return context


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
#         return redirect('user_groups:group_detail', group.pk)


# @permission_required('user_groups.roles_mgmt_permission', raise_exception=True)
# def remove_users_from_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     users = request.POST.getlist('assigned_users')
#     if users:
#         for user in users:
#             group.user_set.remove(user)
#         messages.success(request, 'Successfully done.')
#         return redirect('user_groups:group_detail', group.pk)


class UpdateGroup(PermissionRequiredMixin, generic.UpdateView, SuccessMessageMixin):
    model = Group
    form_class = UserGroupForm
    template_name = 'user_groups/update_group.html'
    success_message = 'Successfully updated.'
    context_object_name = 'group'
    # permission_required = 'user_groups.roles_mgmt_permission'
    permission_required = ''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permissions'] = GlobalPermission.objects.filter(content_type__model='global permission').order_by(
            'name')
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('md-users:groups_list')


class DeleteGroup(PermissionRequiredMixin, generic.DeleteView):
    model = Group
    template_name = 'user_groups/delete_group.html'
    context_object_name = 'group'
    permission_required = ''

    def get_success_url(self) -> str:
        return reverse_lazy('md-users:groups_list')

# # @permission_required('user_groups.roles_mgmt_permission', raise_exception=True)
# def delete_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'POST':
#         group.delete()
#         messages.success(request, 'Successfully deleted.')
#         return redirect('user_groups:list_groups')


