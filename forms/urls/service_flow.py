from django.urls import path
from forms.views.service_flow import ServiceFlowCreateView, ServiceFlowUpdateView

app_name = 'service_flo'
urlpatterns = [
    path('create',
         ServiceFlowCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ServiceFlowUpdateView.as_view(), name='update'),
]
