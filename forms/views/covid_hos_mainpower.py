from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.covid_hospital_manpower import CovidHospitalManpower
from forms.forms.covid_hos_mainpower import CovidHospitalManpowerLine, CovidHospitalmainpowerFormSet


class CovidHospitalMainpowerCreateView(CreateView):
    model = CovidHospitalManpower
    template_name = "forms/covid_hos_mainpower/create.html"
    form_class = CovidHospitalManpowerLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CovidHospitalmainpowerFormSet(self.request.POST)
        else:
            data['lines'] = CovidHospitalmainpowerFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        collection = context.get('collection')
        if collection:
            collection.pcr_kit_usage = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covid_hos_mainpower:create')


class CovidHospitalMainpowerUpdateView(UpdateView):
    model = CovidHospitalManpower
    template_name = "forms/covid_hos_mainpower/update.html"
    form_class = CovidHospitalManpowerLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PcrKitUsageUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = CovidHospitalmainpowerFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = CovidHospitalmainpowerFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
            if collection:
                collection.covid_hos_mainpower = self.object
                collection.save()

            return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('covid_hos_mainpower:update', kwargs={'pk': self.object.pk})
