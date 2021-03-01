from django.urls import path

from forms.views.recover_amount_views import RecoverAmountCreateView, RecoverAmountUpdateView

app_name = 'recover_amount-forms'
urlpatterns = [
    path('create/',
         RecoverAmountCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RecoverAmountUpdateView.as_view(), name='update'),
]
