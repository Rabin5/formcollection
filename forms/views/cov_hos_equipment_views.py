from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import (
    CovidHospitalEquipment,
    Product
)
from forms.forms.cov_hos_equipment_forms import (
    CovidHospitalEquipmentForm,
    CovidHospitalEquipmentLineFormSet
)


class CovidHospitalEquipmentCreateView(CreateView):
    model = CovidHospitalEquipment
    template_name = "forms/cov_hos_equip/create.html"
    form_class = CovidHospitalEquipmentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CovidHospitalEquipmentLineFormSet(
                self.request.POST
            )
        else:
            data['lines'] = CovidHospitalEquipmentLineFormSet()
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
            collection.cov_hos_equip = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covHosEquip-forms:create')


class CovidHospitalEquipmentUpdateView(UpdateView):
    model = CovidHospitalEquipment
    template_name = "forms/cov_hos_equip/update.html"
    form_class = CovidHospitalEquipmentForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_products = [
            'एम्बुलेन्स', 'आइसोलेशन', 'भेन्टिलेटर', 'आईसीयू बेड',
            'पिसीआर मेशीन', 'मास्क', 'पिपीई', 'इन्फ्रारेड थर्मोमिटर',
            'शु कभर', 'क्याप', 'ग्लोव्स', 'गोन मिडियन',
            'ह्णड बुक', 'प्रोटोकल फर्म'
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
        data = super(CovidHospitalEquipmentUpdateView, self).get_context_data(
            **kwargs
        )
        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = CovidHospitalEquipmentLineFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = CovidHospitalEquipmentLineFormSet(
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
            'covHosEquip-forms:update',
            kwargs={'pk': self.object.pk}
        )
