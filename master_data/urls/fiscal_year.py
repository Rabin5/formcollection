from django.urls import path

from master_data.views.fiscal_year import FyCreateView, FyListView, FyUpdateView

app_name = 'md-fy'

urlpatterns = [
    path('', FyListView.as_view(), name='list'),
    path('create/', FyCreateView.as_view(), name='create'),
    path('<int:pk>/update', FyUpdateView.as_view(), name='update'),
]
