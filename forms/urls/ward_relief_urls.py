from django.urls import path

from forms.views.ward_relief_views import WardReliefProcureDistributionCreateView, WardReliefProcureDistributionUpdateView

app_name = 'ward_relief'
urlpatterns = [
    path('create',
         WardReliefProcureDistributionCreateView.as_view(), name='ward_relief_create'),
    path('<int:pk>/update',
         WardReliefProcureDistributionUpdateView.as_view(), name='ward_relief_update'),
]
