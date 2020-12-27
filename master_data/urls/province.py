from django.urls import path

from master_data.views.province_view import ProvinceListView, ProvinceCreateView, ProvinceUpdateView

app_name = 'md-province'

urlpatterns = [
    path('', ProvinceListView.as_view(), name='list'),
    path('create/', ProvinceCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ProvinceUpdateView.as_view(), name='update'),
]
