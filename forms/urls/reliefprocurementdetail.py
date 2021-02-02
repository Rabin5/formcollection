from django.urls import path

from forms.views.reliefprocurementdetail import ReliefProcurementDetailCreateView, ReliefProcurementDetailUpdateView

app_name = 'relief_procu_detail'
urlpatterns = [
    path('create',
         ReliefProcurementDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ReliefProcurementDetailUpdateView.as_view(), name='update'),
]
