from django.urls import path

from forms.views.incomplete_construction_work_views import IncompleteConstructionWorkCreateView, IncompleteConstructionWorkUpdateView

app_name = 'incomplete_construction_work-forms'
urlpatterns = [
    path('create/',
         IncompleteConstructionWorkCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         IncompleteConstructionWorkUpdateView.as_view(), name='update'),
]
