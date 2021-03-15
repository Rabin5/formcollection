from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import NotifyEmployee
from forms.forms.notify_employee_forms import NotifyEmployeeForm, NotifyEmployeeFormSet


class NotifyEmployeeCreateView(CreateView):
    model = NotifyEmployee
    template_name = "forms/notify_employee/create.html"
    form_class = NotifyEmployeeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = NotifyEmployeeFormSet(self.request.POST)
        else:
            data['lines'] = NotifyEmployeeFormSet()
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
            collection.notify_employee = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('notify_employee-forms:create')


class NotifyEmployeeUpdateView(UpdateView):
    model = NotifyEmployee
    template_name = "forms/notify_employee/update.html"
    form_class = NotifyEmployeeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = NotifyEmployeeFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = NotifyEmployeeFormSet(instance=self.object)
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
        return reverse_lazy('notify_employee-forms:update', kwargs={'pk': self.object.pk})
