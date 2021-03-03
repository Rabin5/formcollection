from django.urls import path

from collection.views.cov_hos_form_collection_views import CovHosFormCollectionCreateView, CovHosFormCollectionListView, \
    CovHosFormCollectionDeleteView, CovHosFormCollectionUpdateView, CovHosFormCollectionReview, cov_hos_submit_form, \
        ApproveView, CovHosFormCollectionReportPdf

app_name = 'cov_hos_forms'
urlpatterns = [
    path('create', CovHosFormCollectionCreateView.as_view(), name='cov_hos_create'),
    path('<int:pk>/update', CovHosFormCollectionUpdateView.as_view(), name='cov_hos_update'),
    path('<int:pk>/delete', CovHosFormCollectionDeleteView.as_view(), name='cov_hos_delete'),
    path('', CovHosFormCollectionListView.as_view(), name='cov_hos_list'),
    path('review/<str:action>/<int:pk>', CovHosFormCollectionReview.as_view(), name='review'),
    path('<int:form_pk>/submit', cov_hos_submit_form, name='submit_form'),
    path('approve/', ApproveView.as_view(), name='review_approve_list'),
    path('<int:pk>/report', CovHosFormCollectionReportPdf.as_view(), name='report-covid-hospital-pdf'),
]
