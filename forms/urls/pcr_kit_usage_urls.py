from django.urls import path

from forms.views.pcr_kit_usage_views import PcrKitUsageCreateView, PcrKitUsageUpdateView

app_name = 'pcrKit-forms'
urlpatterns = [
    path('create',
         PcrKitUsageCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         PcrKitUsageUpdateView.as_view(), name='update'),
]
