from django.urls import path

from master_data.views.complaint_type_view import ComplaintTypeCreateView, ComplaintTypeListView,\
    ComplaintTypeUpdateView, ComplaintTypeDeleteView

app_name = 'md-complaint_type'

urlpatterns = [
    path('', ComplaintTypeListView.as_view(), name='list'),
    path('create/', ComplaintTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ComplaintTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ComplaintTypeDeleteView.as_view(), name='delete'),
]
