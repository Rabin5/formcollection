from django.urls import path

from master_data.views.training_center_view import TrainingCenterCreateView, TrainingCenterListView,\
    TrainingCenterUpdateView, TrainingCenterDeleteView

app_name = 'md-training_center'

urlpatterns = [
    path('', TrainingCenterListView.as_view(), name='list'),
    path('create/', TrainingCenterCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TrainingCenterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TrainingCenterDeleteView.as_view(), name='delete'),
]
