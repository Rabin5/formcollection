from django.urls import path

from forms.views. expenditure_detail_views import ExpenditureDetailCreateView, ExpenditureDetailUpdateView

app_name = ' expenditure_detail-forms'
urlpatterns = [
    path('create/',
         ExpenditureDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ExpenditureDetailUpdateView.as_view(), name='update'),
]
