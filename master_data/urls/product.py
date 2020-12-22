from django.urls import path

from master_data.views.product import ProdCreateView, ProdListView, ProdUpdateView,\
    UomCreateView, UomListView, UomUpdateView

app_name = 'md-prod'

urlpatterns = [
    path('', ProdListView.as_view(), name='list'),
    path('create/', ProdCreateView.as_view(), name='create'),
    path('<int:pk>/update', ProdUpdateView.as_view(), name='update'),
    path('uom/', UomListView.as_view(), name='uom_list'),
    path('uom/create/', UomCreateView.as_view(), name='uom_create'),
    path('uom/<int:pk>/update', UomUpdateView.as_view(), name='uom_update'),
]
