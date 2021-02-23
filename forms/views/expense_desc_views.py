from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models import ExpenseDesc
from forms.forms.expense_desc import ExpenseDescForm, ExpenseDescFormSet


class ExpenseDescCreateView(CreateView):
    model = ExpenseDesc
    template_name = "forms/expense_desc/create.html"
    form_class = ExpenseDescForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ExpenseDescFormSet(self.request.POST)
        else:
            data['lines'] = ExpenseDescFormSet()
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

        # collection = context.get('collection')
        # if collection:
        #     collection.expense_desc = self.object
        #     collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('expense_desc-forms:create')


class ExpenseDescUpdateView(UpdateView):
    model = ExpenseDesc
    template_name = "forms/expense_desc/update.html"
    form_class = ExpenseDescForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ExpenseDescFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = ExpenseDescFormSet(instance=self.object)
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
        return reverse_lazy('expense_desc-forms:update', kwargs={'pk': self.object.pk})

