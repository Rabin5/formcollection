from django.urls import path

from users.views.user_views import (
    UserCreateView, UserListView, UserUpdateView,
    ResetPasswordView, ChangePasswordView,
)

from users.views.user_group_views import *

app_name = 'users'

urlpatterns = [
    # Group
    path('list/', UserListView.as_view(), name='list'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    # User Groups
    path('user_groups/create/', CreateGroup.as_view(), name='create_group'),
    path('user_groups/list/', ListGroup.as_view(), name='groups_list'),
    # path('user_groups/<int:pk>/detail/', GroupDetail.as_view(), name='group_detail'),
    path('user_groups/<int:pk>/update/', UpdateGroup.as_view(), name='update_group'),
    # path('user_groups/<int:pk>/assign/users/', assign_users_in_group, name='assign_users_in_group'),
    # path('user_groups/<int:pk>/remove/users/', remove_users_from_group, name='remove_users_from_group'),
    path('user_groups/<int:pk>/delete/', DeleteGroup.as_view(), name='delete_group'),

    # Permission
    path('user_permission/create/', CreatePermissionView.as_view(), name='create_permission'),
    path('user_permission/list/', ListPermissionView.as_view(), name='list_permissions'),
    path('user_permission/<int:pk>/update/', EditPermissionView.as_view(), name='edit_permission'),
    path('user_permission/<int:pk>/delete/', DeletePermission.as_view(), name='delete_permission'),

]