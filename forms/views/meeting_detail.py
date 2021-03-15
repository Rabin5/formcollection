from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.meeting_detail import (
    MeetingDetail
)
from forms.forms.meeting_detail_forms import (
    MeetingDetailForm,
    MeetingDetailLineFormSet
)


class MeetingDetailCreateView(CreateView):
    model = MeetingDetail
    template_name = "forms/meeting_detail/create.html"
    form_class = MeetingDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MeetingDetailLineFormSet(self.request.POST)
        else:
            data['lines'] = MeetingDetailLineFormSet()
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
            collection.meeting_detail = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('meeting_detail:create')


class MeetingDetailUpdateView(UpdateView):
    model = MeetingDetail
    template_name = "forms/meeting_detail/update.html"
    form_class = MeetingDetailForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial  = [
            {
                'meeting_conclusion': 'बैठकको माईन्युटको छायाँ प्रति संलग्न गर्ने।',
            }
        ]

        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = MeetingDetailLineFormSet(
                self.request.POST, instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = MeetingDetailLineFormSet(
                instance=self.object, initial=initial
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
        return self.render_to_response(self.get_context_data(
            form=form,
            lines=lines
        )
        )

    def get_success_url(self):
        return reverse_lazy('meeting_detail:update', kwargs={'pk': self.object.pk})
