from django.urls import path

from master_data.views.grant_type_view import GrantTypeCreateView, GrantTypeListView,\
    GrantTypeUpdateView, GrantTypeDeleteView

app_name = 'md-grant_type'

urlpatterns = [
    path('', GrantTypeListView.as_view(), name='list'),
    path('create/', GrantTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', GrantTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', GrantTypeDeleteView.as_view(), name='delete'),
]
