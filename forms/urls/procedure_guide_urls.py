from django.urls import path

from forms.views.procedure_guide_views import ProcedureGuideCreateView, ProcedureGuideUpdateView

app_name = 'procedure_guide-forms'
urlpatterns = [
    path('create/',
         ProcedureGuideCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ProcedureGuideUpdateView.as_view(), name='update'),
]
