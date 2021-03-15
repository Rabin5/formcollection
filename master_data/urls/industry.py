from django.urls import path

from master_data.views.industry_view import IndustryCreateView, IndustryListView,\
    IndustryUpdateView, IndustryDeleteView

app_name = 'md-industry'

urlpatterns = [
    path('', IndustryListView.as_view(), name='list'),
    path('create/', IndustryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', IndustryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', IndustryDeleteView.as_view(), name='delete'),
]
