from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.forms.judicialcommittee import JudicialCommitteeFormLine, JudicialCommitteeFormSet
from forms.models.judicialcommittee import JudicialCommittee


class JudicialCommitteeCreateView(CreateView):
    model = JudicialCommittee
    template_name = "forms/judicialcommittee/create.html"
    form_class = JudicialCommitteeFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = JudicialCommitteeFormSet(self.request.POST)
        else:
            data['lines'] = JudicialCommitteeFormSet()
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
        return reverse_lazy('judicial-com:create')


class JudicialCommitteeUpdateView(UpdateView):
    model = JudicialCommittee
    template_name = "forms/judicialcommittee/update.html"
    form_class = JudicialCommitteeFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(MedPurchaseDescUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = JudicialCommitteeFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = JudicialCommitteeFormSet(instance=self.object)
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
        return reverse_lazy('judicial-com:update', kwargs={'pk': self.object.pk})
