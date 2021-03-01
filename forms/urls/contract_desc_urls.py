from django.urls import path

from forms.views.contract_desc_views import ContractDescCreateView, ContractDescUpdateView

app_name = 'contract_desc-forms'
urlpatterns = [
    path('create/',
         ContractDescCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ContractDescUpdateView.as_view(), name='update'),
]
