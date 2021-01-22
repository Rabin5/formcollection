from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import MedicalReceipt, MedicalReceiptLine
from forms.forms.medical_receipt import MedicalReceiptForm, MedicalReceiptLineForm, MedicalReceiptFormSet


class MedicalReceiptCreateView(CreateView):
    model = MedicalReceipt
    template_name = "forms/medical_receipt/create.html"
    form_class = MedicalReceiptForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['body'] = GovernmentBody.objects.values_list('name')
        if self.request.POST:
            data['lines'] = MedicalReceiptFormSet(self.request.POST)
        else:
            data['lines'] = MedicalReceiptFormSet()
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
            collection.medical_receipt = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('medical-forms:fre-create')


class MedicalReceiptUpdateView(UpdateView):
    model = MedicalReceipt
    template_name = "forms/medical_receipt/update.html"
    form_class = MedicalReceiptForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedicalReceiptFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = MedicalReceiptFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                # import pdb;pdb.set_trace()
                lines.instance = self.object
                lines.save()
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('medical-forms:medical_receipt-update', kwargs={'pk': self.object.pk})
