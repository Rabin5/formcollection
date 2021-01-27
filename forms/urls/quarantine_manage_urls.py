from django.urls import path

from forms.views.quarantine_management_detail_views import QuarantineManagementDetailCreateView, QuarantineManagementDetailUpdateView

app_name = 'quarantine_forms'
urlpatterns = [
    path('create', QuarantineManagementDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update', QuarantineManagementDetailUpdateView.as_view(), name='update'),
]
