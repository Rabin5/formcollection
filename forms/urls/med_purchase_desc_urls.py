from django.urls import path

from forms.views.med_purchase_desc_views import MedPurchaseDescCreateView, MedPurchaseDescUpdateView

app_name = 'medDesc-forms'
urlpatterns = [
    path('create',
         MedPurchaseDescCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         MedPurchaseDescUpdateView.as_view(), name='update'),
]
