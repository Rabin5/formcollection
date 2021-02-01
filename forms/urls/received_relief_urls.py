from django.urls import path

from forms.views.received_relief_views import ReceivedReliefDetailCreateView, ReceivedReliefDetailUpdateView

app_name = 'received_relief'
urlpatterns = [
    path('create',
         ReceivedReliefDetailCreateView.as_view(), name='received_relief_create'),
    path('<int:pk>/update',
         ReceivedReliefDetailUpdateView.as_view(), name='received_relief_update'),
]
