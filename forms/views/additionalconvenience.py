from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView
from forms.forms.additionalconvenience import AdditionalConvenienceFormLine, AdditionalConvenienceFormSet
from forms.models.additionalconvenience import AdditionalConvenienceLine, AdditionalConvenience


class AdditionalConvenienceCreateView(CreateView):
    model = AdditionalConvenience
    template_name = 'forms/additionalconvenience/create.html'
    form_class = AdditionalConvenienceFormLine
    success_url = None

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = AdditionalConvenienceFormSet(self.request.POST)
        else:
            data['lines'] = AdditionalConvenienceFormSet()
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
            collection.action_plan_implementation = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('asdditional_conven:create')


class AdditionalConvenienceUpdateView(UpdateView):
    model = AdditionalConvenience
    template_name = 'forms/additionalconvenience/update.html'
    form_class = AdditionalConvenienceFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(AdditionalConvenienceUpdateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = AdditionalConvenienceFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = AdditionalConvenienceFormSet(
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
        return reverse_lazy('asdditional_conven:update', kwargs={'pk': self.object.pk})
