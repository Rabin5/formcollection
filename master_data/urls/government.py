from django.urls import path

from master_data.views.government import *

app_name = 'md-gov'

urlpatterns = [
    path('', GovernmentBodyListView.as_view(), name='list'),
    path('create/', GovernmentBodyCreateView.as_view(), name='create'),
    path('<int:pk>/update', GovernmentBodyUpdateView.as_view(), name='update'),
    path('gov_type/', GovernmentBodyTypeListView.as_view(), name='gov_type_list'),
    path('gov_type/create/', GovernmentBodyTypeCreateView.as_view(), name='gov_type_create'),
    path('gov_type/<int:pk>/update', GovernmentBodyTypeUpdateView.as_view(), name='gov_type_update'),
]
