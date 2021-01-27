from django.urls import path

from forms.views.isolationconsexpenditure import IsolationConsExpenditureCreateView, IsolationConsExpenditureUpdateView

app_name = 'iso_cons_expenditure'
urlpatterns = [
    path('create',
         IsolationConsExpenditureCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         IsolationConsExpenditureUpdateView.as_view(), name='update'),
]
