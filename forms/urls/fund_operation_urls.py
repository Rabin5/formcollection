from django.urls import path

from forms.views.fund_operation_views import FundOperationCreateView, FundOperationUpdateView

app_name = 'fund_operation'
urlpatterns = [
    path('create',
         FundOperationCreateView.as_view(), name='fund_operation_create'),
    path('<int:pk>/update',
         FundOperationUpdateView.as_view(), name='fund_operation_update'),
]
