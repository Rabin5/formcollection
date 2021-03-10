from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import (
    FundReceiptExpense,
    SourceBudget,
    ExpenseHeader
)
from forms.forms.fund_receipt_expense_forms import (
    FundReceiptExpenseForm,
    FundReceiptExpenseLineFormset
)


class FundReceiptExpenseCreateView(CreateView):
    model = FundReceiptExpense
    template_name = "forms/fund_receipt_expense/create.html"
    form_class = FundReceiptExpenseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = FundReceiptExpenseLineFormset(self.request.POST)
        else:
            data['lines'] = FundReceiptExpenseLineFormset()
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
            collection.fund_receipt_expense = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fund_receipt_expense:create')


class FundReceiptExpenseUpdateView(UpdateView):
    model = FundReceiptExpense
    template_name = "forms/fund_receipt_expense/update.html"
    form_class = FundReceiptExpenseForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []

        budgets = SourceBudget.objects.all()
        expenses = ExpenseHeader.objects.all().order_by('id')

        for idx, budget in enumerate(budgets):
            line = {
                'budget_source': budget,
                'expense_header': expenses[idx] if idx <= len(expenses)
                else None
            }
            initial.append(line)
        print(initial[0].get('expense_header'))
        return initial

    def get_context_data(self, **kwargs):
        data = super(
            FundReceiptExpenseUpdateView,
            self
        ).get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = FundReceiptExpenseLineFormset(
                self.request.POST, instance=self.object, initial=initial)
        else:
            data['lines'] = FundReceiptExpenseLineFormset(
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
            self.get_context_data(
                form=form,
                lines=lines
            )
        )

    def get_success_url(self):
        return reverse_lazy(
            'fund_receipt_expense:update',
            kwargs={'pk': self.object.pk}
        )
