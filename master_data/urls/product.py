from django.urls import path

from master_data.views.product import ProdCreateView, ProdListView, ProdUpdateView, ProdDeleteView, \
    UomCreateView, UomListView, UomUpdateView, UomDeleteView, \
        ProcurementCreateView, ProcurementListView, ProcurementUpdateView, ProcurementDeleteView

app_name = 'md-prod'

urlpatterns = [
    path('', ProdListView.as_view(), name='list'),
    path('create/', ProdCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ProdUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProdDeleteView.as_view(), name='delete'),
    path('uom/', UomListView.as_view(), name='uom_list'),
    path('uom/create/', UomCreateView.as_view(), name='uom_create'),
    path('uom/<int:pk>/update/', UomUpdateView.as_view(), name='uom_update'),
    path('uom/<int:pk>/delete/', UomDeleteView.as_view(), name='uom_delete'),
    path('procurement/', ProcurementListView.as_view(), name='procurement_list'),
    path('procurement/create/', ProcurementCreateView.as_view(), name='procurement_create'),
    path('procurement/<int:pk>/update/', ProcurementUpdateView.as_view(), name='procurement_update'),
    path('procurement/<int:pk>/delete/', ProcurementDeleteView.as_view(), name='procurement_delete'),
]
