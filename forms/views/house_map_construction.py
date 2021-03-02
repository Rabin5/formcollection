from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.house_map_construction import (
    HouseMapConstructionLine,
    HouseMapConstruction
)
from forms.forms.house_map_construction import (
    HouseMapConstructionFormLine,
    HouseMapConstructionForm,
    HouseMapConstructionLineFormset
)


class HouseMapConstructionCreateView(CreateView):
    model = HouseMapConstructionLine
    template_name = "forms/house_map/create.html"
    form_class = HouseMapConstructionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = HouseMapConstructionLineFormset(self.request.POST)
        else:
            data['lines'] = HouseMapConstructionLineFormset()
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
            collection.medical_use = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('house_map:create')


class HouseMapConstructionUpdateView(UpdateView):
    model = HouseMapConstruction
    template_name = "forms/house_map/update.html"
    form_class = HouseMapConstructionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = HouseMapConstructionLineFormset(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = HouseMapConstructionLineFormset(
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
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('house_map:update', kwargs={'pk': self.object.pk})
