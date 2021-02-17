from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView
from forms.forms.action_plan_implementation_forms import (
    ActionPlanImplementationForm,
    ActionPlanImplementationLineForm,
    ActionPlanImplementationFormSet
)
from forms.models.action_plan_implementation import (
    ActionPlanImplementation,
    ActionPlanActivity
)


class ActionPlanImplementationCreateView(CreateView):
    model = ActionPlanImplementation
    template_name = 'forms/action_plan_implementation/create.html'
    form_class = ActionPlanImplementationForm
    success_url = None

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ActionPlanImplementationFormSet(self.request.POST)
        else:
            data['lines'] = ActionPlanImplementationFormSet()
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
        return reverse_lazy('action_plan_forms:create')


class ActionPlanImplementationUpdateView(UpdateView):
    model = ActionPlanImplementation
    template_name = 'forms/action_plan_implementation/update.html'
    form_class = ActionPlanImplementationForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_activities = ActionPlanActivity.objects.all()

        for activity in initial_activities:
            line = {
                'activity': activity
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super(
            ActionPlanImplementationUpdateView,
            self
        ).get_context_data(**kwargs)
        
        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = ActionPlanImplementationFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = ActionPlanImplementationFormSet(
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
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('action_plan_forms:update', kwargs={'pk': self.object.pk})
