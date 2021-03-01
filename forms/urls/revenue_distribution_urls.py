from django.urls import path

from forms.views.revenue_distribution_views import RevenueDistributiontCreateView, RevenueDistributiontUpdateView

app_name = 'revenue_distribution-forms'
urlpatterns = [
    path('create/',
         RevenueDistributiontCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RevenueDistributiontUpdateView.as_view(), name='update'),
]
