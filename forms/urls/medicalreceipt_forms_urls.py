from django.urls import path

from forms.views.medical_receipt import MedicalReceiptCreateView, MedicalReceiptUpdateView

app_name = 'medical-forms'
urlpatterns = [
    path('create/',
         MedicalReceiptCreateView.as_view(), name='medical_receipt-create'),
    path('<int:pk>/update',
         MedicalReceiptUpdateView.as_view(), name='medical_receipt-update'),
]
