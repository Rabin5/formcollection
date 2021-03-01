from django.urls import path

from master_data.views.work_nature_view import WorkNatureCreateView, WorkNatureListView,\
    WorkNatureUpdateView, WorkNatureDeleteView

app_name = 'md-work_nature'

urlpatterns = [
    path('', WorkNatureListView.as_view(), name='list'),
    path('create/', WorkNatureCreateView.as_view(), name='create'),
    path('<int:pk>/update/', WorkNatureUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', WorkNatureDeleteView.as_view(), name='delete'),
]
