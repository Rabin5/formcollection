from collection.views.province_form_collection_views import (
    ProvinceFormCollectionCreateView, ProvinceFormCollectionDeleteView,
    ProvinceFormCollectionListView, ProvinceFormCollectionReviewView,
    ProvinceFormCollectionUpdateView, province_submit_form, ApproveView,
    ProvinceFormCollectionReportPdf)
from django.urls import path


app_name = 'province_forms'
urlpatterns = [
    path('create', ProvinceFormCollectionCreateView.as_view(), name='province_create'),
    path('<int:pk>/update', ProvinceFormCollectionUpdateView.as_view(), name='province_update'),
    path('<int:pk>/delete', ProvinceFormCollectionDeleteView.as_view(), name='province_delete'),
    path('', ProvinceFormCollectionListView.as_view(), name='province_list'),
    path('<int:pk>/review/<str:action>', ProvinceFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', province_submit_form, name='submit_form'),
    path('approve/', ApproveView.as_view(), name='review_approve_list'),
    path('<int:pk>/report', ProvinceFormCollectionReportPdf.as_view(), name='report-province-pdf'),
]
