from django.urls import path

from forms.views.integral_advancement_views import IntegralAdvancementCreateView, IntegralAdvancementUpdateView

app_name = 'integral_advancement-forms'
urlpatterns = [
    path('create/',
         IntegralAdvancementCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         IntegralAdvancementUpdateView.as_view(), name='update'),
]
