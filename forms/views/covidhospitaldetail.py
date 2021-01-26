from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.covidhospitaldetail import CovidHospitalDetail
from forms.forms.covidhospitaldetail import CovidHospitalDetailLine, CovidHospitaldetatilFormSet


class CovidHospitalDetailCreateView(CreateView):
    model = CovidHospitalDetail
    template_name = "forms/covid_hospital/create.html"
    form_class = CovidHospitalDetailLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CovidHospitaldetatilFormSet(self.request.POST)
        else:
            data['lines'] = CovidHospitaldetatilFormSet()
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
            collection.covidhospitaldetail = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covid_hos_detail:create')


class CovidHospitalDetailUpdateView(UpdateView):
    model = CovidHospitalDetail
    template_name = "forms/covid_hospital/update.html"
    form_class = CovidHospitalDetailLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CovidHospitalDetailUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = CovidHospitaldetatilFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = CovidHospitaldetatilFormSet(instance=self.object)
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
                collection.isolationconstructonexpenditure = self.object
                collection.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covid_hos_detail:create',)
