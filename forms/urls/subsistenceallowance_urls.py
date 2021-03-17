from django.urls import path

from forms.views.subsistenceallowance_view import SubsistenceAllowanceCreateView, SubsistenceAllowanceUpdateView

app_name = 'subsistence_allowance'
urlpatterns = [
    path('create', SubsistenceAllowanceCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         SubsistenceAllowanceUpdateView.as_view(), name='update'),
]
