from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.forms.districtcovid_management import DistrictCovidManagementForm, DistrictCovidIsolManagementFormSet, DistrictCovidLabtTestManagementFormSet, DistrictCovidQuaManagementFormSet
from forms.models.districtcovidmanagement import DistrictCovidManagement


class DistrictCovidManagementCreateView(CreateView):
    model = DistrictCovidManagement
    template_name = "forms/covid_district_management/create.html"
    form_class = DistrictCovidManagementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(DistrictCovidManagementCreateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['isolationlines'] = DistrictCovidIsolManagementFormSet(
                self.request.POST)
            data['quarentinelines'] = DistrictCovidQuaManagementFormSet(
                self.request.POST)
            data['labtestlines'] = DistrictCovidLabtTestManagementFormSet(
                self.request.POST)
        else:
            data['isolationlines'] = DistrictCovidIsolManagementFormSet()
            data['quarentinelines'] = DistrictCovidQuaManagementFormSet()
            data['labtestlines'] = DistrictCovidLabtTestManagementFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        iso_lines = context['isolationlines']
        qua_lines = context['quarentinelines']
        lab_lines = context['labtestlines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if iso_lines.is_valid() and qua_lines.is_valid() and lab_lines.is_valid():
                iso_lines.instance = self.object
                qua_lines.instance = self.object
                lab_lines.instance = self.object
                iso_lines.save()
                qua_lines.save()
                lab_lines.save()
        collection = context.get('collection')
        if collection:
            collection.district_covid_management = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('district_covid_management:create')


class DistrictCovidManagementUpdateView(UpdateView):
    model = DistrictCovidManagement
    template_name = "forms/covid_district_management/update.html"
    form_class = DistrictCovidManagementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(DistrictCovidManagementUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['isolationlines'] = DistrictCovidIsolManagementFormSet(
                self.request.POST, instance=self.object)
            data['quarentinelines'] = DistrictCovidQuaManagementFormSet(
                self.request.POST, instance=self.object)
            data['labtestlines'] = DistrictCovidLabtTestManagementFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['isolationlines'] = DistrictCovidIsolManagementFormSet(instance=self.object)
            data['quarentinelines'] = DistrictCovidQuaManagementFormSet(instance=self.object)
            data['labtestlines'] = DistrictCovidLabtTestManagementFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        iso_lines = context['isolationlines']
        qua_lines = context['quarentinelines']
        lab_lines = context['labtestlines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if iso_lines.is_valid() and qua_lines.is_valid() and lab_lines.is_valid():
                iso_lines.instance = self.object
                qua_lines.instance = self.object
                lab_lines.instance = self.object
                iso_lines.save()
                qua_lines.save()
                lab_lines.save()
            else:
                return self.form_invalid(form, iso_lines)

            return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('district_covid_management:update', kwargs={'pk': self.object.pk})
