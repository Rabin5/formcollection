from django.urls import path

from master_data.views.project_type_view import ProjectTypeCreateView, ProjectTypeListView,\
    ProjectTypeUpdateView, ProjectTypeDeleteView

app_name = 'md-project_type'

urlpatterns = [
    path('', ProjectTypeListView.as_view(), name='list'),
    path('create/', ProjectTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ProjectTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProjectTypeDeleteView.as_view(), name='delete'),
]
