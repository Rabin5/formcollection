from django.urls import path

from master_data.views.designation_view import DesignationCreateView, DesignationListView,\
    DesignationUpdateView, DesignationDeleteView

app_name = 'md-designation'

urlpatterns = [
    path('', DesignationListView.as_view(), name='list'),
    path('create/', DesignationCreateView.as_view(), name='create'),
    path('<int:pk>/update/', DesignationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DesignationDeleteView.as_view(), name='delete'),
]
