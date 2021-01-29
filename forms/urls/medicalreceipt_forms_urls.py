from django.urls import path

from forms.views.medical_receipt import MedicalReceiptCreateView, MedicalReceiptUpdateView

app_name = 'medical_receipt-forms'
urlpatterns = [
    path('create/',
         MedicalReceiptCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         MedicalReceiptUpdateView.as_view(), name='update'),
]
