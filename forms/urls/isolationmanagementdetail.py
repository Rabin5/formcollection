from django.urls import path

from forms.views.isolationmanagementdetail import IsolationdetailMangementCreateView, IsolationdetailMangementUpdateView

app_name = 'iso_mgt_detail'
urlpatterns = [
    path('create', IsolationdetailMangementCreateView.as_view(), name='create'),
    path('<int:pk>/update', IsolationdetailMangementUpdateView.as_view(), name='update'),
]
