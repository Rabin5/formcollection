from django.urls import path

from collection.views.province_form_collection_views import ProvinceFormCollectionCreateView, ProvinceFormCollectionListView, \
    ProvinceFormCollectionDeleteView, ProvinceFormCollectionUpdateView

app_name = 'province_forms'
urlpatterns = [
    path('create', ProvinceFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', ProvinceFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ProvinceFormCollectionDeleteView.as_view(), name='delete'),
    path('list', ProvinceFormCollectionListView.as_view(), name='list'),
]
