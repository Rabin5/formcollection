from django.urls import path
from forms.views.cashforwork_views import CashForWorkCreateView, CashForWorkUpdateView

app_name = 'cashfor_work'
urlpatterns = [
    path('create/',
         CashForWorkCreateView.as_view(), name='create'),
    path('<int:pk>/update/',
         CashForWorkUpdateView.as_view(), name='update'),
]
