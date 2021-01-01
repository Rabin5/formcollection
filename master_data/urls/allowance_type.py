from django.urls import path

from master_data.views.allowance_type_view import AllowanceTypeListView, AllowanceTypeCreateView, AllowanceTypeUpdateView

app_name = 'md-allowance_type'

urlpatterns = [
    path('', AllowanceTypeListView.as_view(), name='list'),
    path('create/', AllowanceTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         AllowanceTypeUpdateView.as_view(), name='update'),
]
