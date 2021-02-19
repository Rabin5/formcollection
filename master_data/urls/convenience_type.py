from django.urls import path

from master_data.views.convenience_type_view import ConvenienceTypeCreateView, ConvenienceTypeListView,\
    ConvenienceTypeUpdateView, ConvenienceTypeDeleteView

app_name = 'md-convenience_type'

urlpatterns = [
    path('', ConvenienceTypeListView.as_view(), name='list'),
    path('create/', ConvenienceTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ConvenienceTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ConvenienceTypeDeleteView.as_view(), name='delete'),
]
