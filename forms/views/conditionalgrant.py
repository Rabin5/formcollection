from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView
from forms.forms.conditionalgrant import ConditionalGrantFormLine, ConditionalGrantFormSet
from forms.models.conditionalgrant import ConditionalGrantLine, ConditionalGrant


class ConditionalGrantCreateView(CreateView):
    model = ConditionalGrant
    template_name = 'forms/conditional_grant/create.html'
    form_class = ConditionalGrantFormLine
    success_url = None

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ConditionalGrantFormSet(self.request.POST)
        else:
            data['lines'] = ConditionalGrantFormSet()
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
        return reverse_lazy('cnl_grant:create')


class ConditionalGrantUpdateView(UpdateView):
    model = ConditionalGrant
    template_name = 'forms/conditional_grant/update.html'
    form_class = ConditionalGrantFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ConditionalGrantUpdateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ConditionalGrantFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = ConditionalGrantFormSet(
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
        return reverse_lazy('cnl_grant:update', kwargs={'pk': self.object.pk})
