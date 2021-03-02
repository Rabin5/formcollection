from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import (
    MedicalPurchaseDescription,
    Product
)

from forms.forms.med_purchase_desc_forms import (
    MedPurchaseDescForm,
    MedPurchaseDescLineFormSet
)


class MedPurchaseDescCreateView(CreateView):
    model = MedicalPurchaseDescription
    template_name = "forms/med_purchase_desc/create.html"
    form_class = MedPurchaseDescForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedPurchaseDescLineFormSet(
                self.request.POST
                )
        else:
            data['lines'] = MedPurchaseDescLineFormSet()
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
            collection.med_purchase_desc = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('medDesc-forms:create')


class MedPurchaseDescUpdateView(UpdateView):
    model = MedicalPurchaseDescription
    template_name = "forms/med_purchase_desc/update.html"
    form_class = MedPurchaseDescForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_products = [
            'पिपीई', 'मास्क', 'पिसीआर किट',
            'भिटीएम', 'आरडीटी किट', 'इन्फ्रारेड थर्मोमिटर',
            'भेन्टिलेटर', 'आईसीयू बेड', 'पिसीआर मेशीन'
        ]

        products = Product.objects.filter(
            name__in=initial_products
        )

        for product in products:
            line = {
                'product': product
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super(
                MedPurchaseDescUpdateView,
                self
            ).get_context_data(
                **kwargs
            )

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = MedPurchaseDescLineFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
                )
        else:
            data['lines'] = MedPurchaseDescLineFormSet(
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
        return self.render_to_response(self.get_context_data(
            form=form,
            lines=lines
            ))

    def get_success_url(self):
        return reverse_lazy(
            'medDesc-forms:update',
            kwargs={'pk': self.object.pk}
            )
