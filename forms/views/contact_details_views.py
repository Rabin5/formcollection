from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.contact_details import (
    ContactDetails
)
from forms.forms.contact_details_forms import (
    ContactDetailsForm,
    ContactDetailsLineFormSet
)


class ContactDetailsCreateView(CreateView):
    model = ContactDetails
    template_name = "forms/contact_details/create.html"
    form_class = ContactDetailsForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ContactDetailsLineFormSet(self.request.POST)
        else:
            data['lines'] = ContactDetailsLineFormSet()
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
            collection.contact_details = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contact_details:create')


class ContactDetailsUpdateView(UpdateView):
    model = ContactDetails
    template_name = "forms/contact_details/update.html"
    form_class = ContactDetailsForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial  = []
        initial_service = [
            'गाउपालिका अध्यक्ष्य वा नगरपालिका प्रमुख',
            'लेखा प्रमुख',
            'रोजगार संयोजक'
        ]


        for description in initial_service:
            line = {
                'designation': description
            }
            initial.append(line)
        # initial = [
        #     {'designation': 'गाउपालिका अध्यक्ष्य वा नगरपालिका प्रमुख'}
        # ]

        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = ContactDetailsLineFormSet(
                self.request.POST, instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = ContactDetailsLineFormSet(
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
        return reverse_lazy('contact_details:update', kwargs={'pk': self.object.pk})
