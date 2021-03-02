from collection.views.local_level_form_collection_views import (
    LocalLevelFormCollectionCreateView, LocalLevelFormCollectionDeleteView,
    LocalLevelFormCollectionListView, LocalLevelFormCollectionReviewView,
    LocalLevelFormCollectionUpdateView, local_level_submit_form,
    ApproveView, LocalLevelFormCollectionReportPdf)
from django.urls import path

app_name = 'local_level_forms'
urlpatterns = [
    path('create', LocalLevelFormCollectionCreateView.as_view(), name='local_level_create'),
    path('<int:pk>/update', LocalLevelFormCollectionUpdateView.as_view(), name='local_level_update'),
    path('<int:pk>/delete', LocalLevelFormCollectionDeleteView.as_view(), name='local_level_delete'),
    path('', LocalLevelFormCollectionListView.as_view(), name='local_level_list'),
    path('<int:pk>/review/<str:action>', LocalLevelFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', local_level_submit_form, name='submit_form'),
    path('approve/', ApproveView.as_view(), name='review_approve_list'),
    path('<int:pk>/report', LocalLevelFormCollectionReportPdf.as_view(), name='report-local-level-pdf'),
]
