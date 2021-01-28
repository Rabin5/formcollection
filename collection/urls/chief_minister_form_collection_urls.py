from django.urls import path

from collection.views.chief_minister_form_collection_views import ChiefMinisterOfficeFormCollectionCreateView, ChiefMinisterOfficeFormCollectionListView, \
    ChiefMinisterOfficeFormCollectionDeleteView, ChiefMinisterOfficeFormCollectionUpdateView

app_name = 'chief_minister_forms'
urlpatterns = [
    path('create', ChiefMinisterOfficeFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', ChiefMinisterOfficeFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ChiefMinisterOfficeFormCollectionDeleteView.as_view(), name='delete'),
    path('list', ChiefMinisterOfficeFormCollectionListView.as_view(), name='list'),
]
