from django.urls import path

from master_data.views.sub_header_view import SubHeaderCreateView, SubHeaderListView,\
    SubHeaderUpdateView, SubHeaderDeleteView

app_name = 'md-sub_header'

urlpatterns = [
    path('', SubHeaderListView.as_view(), name='list'),
    path('create/', SubHeaderCreateView.as_view(), name='create'),
    path('<int:pk>/update/', SubHeaderUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SubHeaderDeleteView.as_view(), name='delete'),
]
