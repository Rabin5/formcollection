from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.vechile_purches import (
    VehiclePurchase,
    VehiclePurchaseLine
)
from forms.forms.vechile_purches import (
    VehiclePurchaseFormLine,
    VehiclePurchaseFormSet
)


class VehiclePurchaseCreateView(CreateView):
    model = VehiclePurchase
    template_name = "forms/vechile_purches/create.html"
    form_class = VehiclePurchaseFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = VehiclePurchaseFormSet(
                self.request.POST
            )
        else:
            data['lines'] = VehiclePurchaseFormSet()
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
        return reverse_lazy('vechile_pur:create')


class VehiclePurchaseUpdateView(UpdateView):
    model = VehiclePurchase
    template_name = "forms/vechile_purches/update.html"
    form_class = VehiclePurchaseFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = VehiclePurchaseFormSet(
                self.request.POST, instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = VehiclePurchaseFormSet(
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
        return reverse_lazy('vechile_pur:update', kwargs={'pk': self.object.pk})
