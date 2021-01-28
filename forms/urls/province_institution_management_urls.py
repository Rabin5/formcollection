from django.urls import path

from forms.views.province_institution_management_views import (
    ProvinceInstitutionManagementCreateView,
    ProvinceInstitutionManagementUpdateView,
)


app_name = "province_institution_management"

urlpatterns = [
    path("create", ProvinceInstitutionManagementCreateView.as_view(), name="create"),
    path(
        "<int:pk>/update",
        ProvinceInstitutionManagementUpdateView.as_view(),
        name="update",
    ),
]
