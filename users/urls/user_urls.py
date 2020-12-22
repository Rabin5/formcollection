from django.urls import path

from users.views.user_views import (
    UserCreateView, UserListView, UserUpdateView,
    ResetPasswordView, ChangePasswordView,
)

app_name = 'md-users'

urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),

    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]