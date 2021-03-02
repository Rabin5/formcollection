from django.urls import path
from forms.views.vechile_purches import VehiclePurchaseCreateView, VehiclePurchaseUpdateView

app_name = 'vechile_pur'
urlpatterns = [
    path('create',
         VehiclePurchaseCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         VehiclePurchaseUpdateView.as_view(), name='update'),
]
