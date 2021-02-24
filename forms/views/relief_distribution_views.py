from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.relief_distribution_expense import (
    ReliefDistributionExpense,
    ReliefType
)
from forms.forms.relief_distribution_forms import (
    ReliefDistributionExpenseForm,
    ReliefDistributionExpenseFormSet
)


class ReliefDistributionExpenseCreateView(CreateView):
    model = ReliefDistributionExpense
    template_name = "forms/relief_distribution/create.html"
    form_class = ReliefDistributionExpenseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ReliefDistributionExpenseFormSet(
                self.request.POST)
        else:
            data['lines'] = ReliefDistributionExpenseFormSet()
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
            collection.relief_distribution_expense = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('relief_distribution:relief_distribution_create')


class ReliefDistributionExpenseUpdateView(UpdateView):
    model = ReliefDistributionExpense
    template_name = "forms/relief_distribution/update.html"
    form_class = ReliefDistributionExpenseForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_relieftypes = ReliefType.objects.all()[:4]

        for relieftype in initial_relieftypes:
            line = {
                'relief_type': relieftype
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = ReliefDistributionExpenseFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = ReliefDistributionExpenseFormSet(
                instance=self.object,
                initial=initial
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
        return self.render_to_response(
            self.get_context_data(form=form, lines=lines)
        )

    def get_success_url(self):
        return reverse_lazy(
            'relief_distribution:relief_distribution_update',
            kwargs={'pk': self.object.pk}
        )
