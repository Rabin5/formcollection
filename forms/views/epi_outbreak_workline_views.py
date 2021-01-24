from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView
from forms.forms.epidemic_outbreak_preparatory_workline_forms import EpidemicOutbreakPreparatoryWorkLineForm, EpidemicOutbreakPreparatoryWorkForm, EpidemicWorkLineFormSet
from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork


class EpidemicOutbreakWorklineCreateView(CreateView):
    model = EpidemicOutbreakPreparatoryWork
    template_name = 'forms/epi_outbreak_workline/create.html'
    form_class = EpidemicOutbreakPreparatoryWorkForm
    success_url = None

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = EpidemicWorkLineFormSet(self.request.POST)
        else:
            data['lines'] = EpidemicWorkLineFormSet()
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
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('epidemic_forms:epidemic_outbreak_workline-create')


class EpidemicOutbreakWorklineUpdateView(UpdateView):
    model = EpidemicOutbreakPreparatoryWork
    template_name = 'forms/epi_outbreak_workline/update.html'
    form_class = EpidemicOutbreakPreparatoryWorkForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(EpidemicOutbreakWorklineUpdateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = EpidemicWorkLineFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = EpidemicWorkLineFormSet(instance=self.object)
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
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('epidemic_forms:epidemic_outbreak_workline-update', kwargs={'pk': self.object.pk})
