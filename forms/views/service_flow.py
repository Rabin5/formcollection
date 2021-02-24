from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.service_flow import (
    ServiceFlowLine,
    ServiceFlow
)
from forms.forms.service_flow import (
    ServiceFlowFormLine,
    ServiceFlowLineFormSet
)


class ServiceFlowCreateView(CreateView):
    model = ServiceFlow
    template_name = "forms/service_flow/create.html"
    form_class = ServiceFlowFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ServiceFlowLineFormSet(self.request.POST)
        else:
            data['lines'] = ServiceFlowLineFormSet()
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
            collection.risk_allowance = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('service_flo:create')


class ServiceFlowUpdateView(UpdateView):
    model = ServiceFlow
    template_name = "forms/service_flow/update.html"
    form_class = ServiceFlowFormLine
    success_url = None

    # def _get_initial_data(self):
    #     if self.object.lines.all():
    #         return None

    #     initial = []
    #     bearers = ServiceFlow.objects.all()[:5]

    #     for bearer in bearers:
    #         line = {
    #             'office_bearer': bearer
    #         }
    #         initial.append(line)

    #     return initial
    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_service = [
            'नागरिकता सिफारिस', 'घरबाटो सिफारिस', 'नाता प्रमाणित', 'जन्म', 'मृत्यु दर्ता', 'अन्य'
        ]

        service = ServiceFlow.objects.filter(
            name__in=initial_service
        )

        for service in service:
            line = {
                'description': service
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = ServiceFlowLineFormSet(
                self.request.POST, instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = ServiceFlowLineFormSet(
                instance=self.object, initial=initial
            )
            data['lines'].extra = len(initial) if initial else 1
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
        )
        )

    def get_success_url(self):
        return reverse_lazy('service_flo:update', kwargs={'pk': self.object.pk})
