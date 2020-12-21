from django.urls import path

from master_data.views.product import ProdCreateView, ProdListView, ProdUpdateView

app_name = 'md-prod'

urlpatterns = [
    path('', ProdListView.as_view(), name='list'),
    path('create/', ProdCreateView.as_view(), name='create'),
    path('<int:pk>/update', ProdUpdateView.as_view(), name='update'),
]
