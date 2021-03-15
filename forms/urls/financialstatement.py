from django.urls import path
from forms.views.financialstatement_view import (
    Financial_St_ResCreateView, Financial_St_ResUpdateView)
app_name = 'finalcial_statement'
urlpatterns = [
    path('create/',
         Financial_St_ResCreateView.as_view(), name='create'),
    path('<int:pk>/update/',
         Financial_St_ResUpdateView.as_view(), name='update'),
]
