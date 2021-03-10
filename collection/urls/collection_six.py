from collection.views.collection_six import (
    CollectionSixFormCreateView,
    CollectionSixFormDeleteView,
    CollectionSixFormListView,
    CollectionSixFormReviewView,
    CollectionSixFormUpdateView,
    collection_six_submit_form,
    ApproveView,
    CollectionSixReportPdf)
from django.urls import path

app_name = 'collection_six'
urlpatterns = [
    path('create/', CollectionSixFormCreateView.as_view(),
         name='collection_six_create'),
    path('approve/', ApproveView.as_view(), name='collection_six_approve'),
    path('<int:pk>/update', CollectionSixFormUpdateView.as_view(),
         name='collection_six_update'),
    path('<int:pk>/delete', CollectionSixFormDeleteView.as_view(),
         name='collection_six_delete'),
    path('<int:pk>/review/<str:action>',
         CollectionSixFormReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', collection_six_submit_form, name='submit_form'),
    path('<int:pk>/report', CollectionSixReportPdf.as_view(),
         name='report-collection_six-office-pdf'),
    path('', CollectionSixFormListView.as_view(), name='collection_six_list'),
]
