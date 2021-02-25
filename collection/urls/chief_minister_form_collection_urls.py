from collection.views.chief_minister_form_collection_views import (
    ChiefMinisterOfficeFormCollectionCreateView,
    ChiefMinisterOfficeFormCollectionDeleteView,
    ChiefMinisterOfficeFormCollectionListView,
    ChiefMinisterOfficeFormCollectionReviewView,
    ChiefMinisterOfficeFormCollectionUpdateView, 
    chief_minister_submit_form,
    ApproveView,
    ChiefMinisterOfficeFormCollectionReportPdf)
from django.urls import path

app_name = 'chief_minister_forms'
urlpatterns = [
    path('create', ChiefMinisterOfficeFormCollectionCreateView.as_view(), name='chief_minister_create'),
    path('<int:pk>/update', ChiefMinisterOfficeFormCollectionUpdateView.as_view(), name='chief_minister_update'),
    path('<int:pk>/delete', ChiefMinisterOfficeFormCollectionDeleteView.as_view(), name='chief_minister_delete'),
    path('', ChiefMinisterOfficeFormCollectionListView.as_view(), name='chief_minister_list'),
    path('<int:pk>/review/<str:action>', ChiefMinisterOfficeFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', chief_minister_submit_form, name='submit_form'),
    path('approve/', ApproveView.as_view(), name='review_approve_list'),
    path('<int:pk>/report', ChiefMinisterOfficeFormCollectionReportPdf.as_view(), name='report-chief-minister-office-pdf'),
]
