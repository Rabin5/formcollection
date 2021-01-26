

from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.isolationmanagementdetail import IsolationManagementDetail
from forms.forms.isolationmanagementdetail import IsolationDetailManagementLine, IsolationManagementDetailFormSet


class IsolationdetailMangementCreateView(CreateView):
    model = IsolationManagementDetail
    template_name = "forms/isolation_management/create.html"
    form_class = IsolationDetailManagementLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = IsolationManagementDetailFormSet(self.request.POST)
        else:
            data['lines'] = IsolationManagementDetailFormSet()
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
            collection.pcr_kit_usage = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('iso_mgt_detail:create')


class IsolationdetailMangementUpdateView(UpdateView):
    model = IsolationManagementDetail
    template_name = "forms/pcr_kit_usage/update.html"
    form_class = IsolationDetailManagementLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(IsolationdetailMangementUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = IsolationManagementDetailFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = IsolationManagementDetailFormSet(
                instance=self.object)
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
                collection.isolationmanagementdetail = self.object
                collection.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('iso_mgt_detail:update')
