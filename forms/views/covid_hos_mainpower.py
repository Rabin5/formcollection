from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.covid_hospital_manpower import (
    CovidHospitalManpower,
    Manpower
)
from forms.forms.covid_hos_mainpower import (
    CovidHospitalManpowerForm,
    CovidHospitalmainpowerFormSet
)


class CovidHospitalMainpowerCreateView(CreateView):
    model = CovidHospitalManpower
    template_name = "forms/covid_hos_mainpower/create.html"
    form_class = CovidHospitalManpowerForm
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
            collection.covid_hos_mainpower = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covid_hos_mainpower:create')


class CovidHospitalMainpowerUpdateView(UpdateView):
    model = CovidHospitalManpower
    template_name = "forms/covid_hos_mainpower/update.html"
    form_class = CovidHospitalManpowerForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []

        manpowers = Manpower.objects.all()[:7]

        for manpower in manpowers:
            line = {
                'manpower': manpower
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super(CovidHospitalMainpowerUpdateView, self).get_context_data(
            **kwargs
        )
        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = CovidHospitalmainpowerFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = CovidHospitalmainpowerFormSet(
                instance=self.object,
                initial=initial
            )
            data['lines'].extra = len(initial) + 1 if initial else 1
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
            else:
                return self.form_invalid(form, lines)

            return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(
            form=form,
            lines=lines
        ))

    def get_success_url(self):
        return reverse_lazy(
            'covid_hos_mainpower:update',
            kwargs={'pk': self.object.pk}
        )
