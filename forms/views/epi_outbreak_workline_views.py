from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView
from forms.forms.epidemic_outbreak_preparatory_workline_forms import EpidemicOutbreakPreparatoryWorkLineForm, EpidemicOutbreakPreparatoryWorkForm, EpidemicWorkLineFormSet
from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWorkLine


class EpidemicOutbreakWorklineCreateView(CreateView):
    model = EpidemicOutbreakPreparatoryWorkLine
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
