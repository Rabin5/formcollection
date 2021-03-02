from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.forms.province_institution_management_forms import (
    ProvinceInstitutionManagementForm,
    ProvinceInstitutionManagementLineFormSet,
)
from forms.models.province_institution_management import (
    ProvinceInstitutionManagement,
)


class ProvinceInstitutionManagementCreateView(CreateView):
    model = ProvinceInstitutionManagement
    template_name = "forms/province_institution_management/create.html"
    form_class = ProvinceInstitutionManagementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["lines"] = ProvinceInstitutionManagementLineFormSet(
                self.request.POST
            )
        else:
            data["lines"] = ProvinceInstitutionManagementLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context["lines"]
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()

        collection = context.get("collection")
        if collection:
            collection.province_institute_management = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("province_institution_management:create")


class ProvinceInstitutionManagementUpdateView(UpdateView):
    model = ProvinceInstitutionManagement
    template_name = "forms/province_institution_management/update.html"
    form_class = ProvinceInstitutionManagementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["lines"] = ProvinceInstitutionManagementLineFormSet(
                self.request.POST, instance=self.object
            )
        else:
            data["lines"] = ProvinceInstitutionManagementLineFormSet(
                instance=self.object
            )
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context["lines"]
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(
            self.get_context_data(form=form, lines=lines)
        )

    def get_success_url(self):
        return reverse_lazy(
            "province_institution_management:update",
            kwargs={"pk": self.object.pk}
        )
