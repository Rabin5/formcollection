from django.urls import path

from forms.views.relief_procure_dist import ReliefProcureDistributionCreateView, ReliefProcureDistributionUpdateView

app_name = 'relief_procure_dis'
urlpatterns = [
    path('create',
         ReliefProcureDistributionCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ReliefProcureDistributionUpdateView.as_view(), name='update'),
]
