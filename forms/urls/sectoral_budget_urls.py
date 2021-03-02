from django.urls import path

from forms.views.sectoral_budget_views import SectoralBudgetCreateView, SectoralBudgetUpdateView

app_name = 'sectoral_budget-forms'
urlpatterns = [
    path('create/',
         SectoralBudgetCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         SectoralBudgetUpdateView.as_view(), name='update'),
]
