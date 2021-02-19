from django.urls import path

from master_data.views.school_view import SchoolCreateView, SchoolListView,\
    SchoolUpdateView, SchoolDeleteView

app_name = 'md-school'

urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    path('create/', SchoolCreateView.as_view(), name='create'),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SchoolDeleteView.as_view(), name='delete'),
]
