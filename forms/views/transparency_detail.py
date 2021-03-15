from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.transparency_detail import (
    TransparencyDetail
)
from forms.forms.transparency_detail_forms import (
    TransparencyDetailForm,
    TransparencyDetailLineFormSet
)


class TransparencyDetailCreateView(CreateView):
    model = TransparencyDetail
    template_name = "forms/transparency_detail/create.html"
    form_class = TransparencyDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = TransparencyDetailLineFormSet(self.request.POST)
        else:
            data['lines'] = TransparencyDetailLineFormSet()
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
            collection.transparency_detail = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('transparency_detail:create')


class TransparencyDetailUpdateView(UpdateView):
    model = TransparencyDetail
    template_name = "forms/transparency_detail/update.html"
    form_class = TransparencyDetailForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        initial_service = [
            'रोजगार व्यवस्थापन सूचना प्रणाली स्थापित र अध्यावधिक, ',
            'स्थानीय तहले श्रमिक समुहको हाजिरी विवरण, भुक्तानी प्राप्त गर्ने श्रमिकको नाम, प्राप्त रकम र खर्चको विवरणको सार्वजनिक परिक्षण गराएको, ',
            'रोजगार आयोजनाहरुको लागत तथा खर्च, श्रमिकको रोजगारीको दिन र भुक्तानीको अद्यावाधिक विवरण रोजगार व्यवस्थापन सूचना प्रणालीमा अध्यावधिक रुपमा प्रविष्टी गरेको। ',
            'स्थानीय तहले आफ्नो क्षेत्रभित्रका कार्यक्रमहरुको सम्बन्धमा कार्यक्रमका लाभग्राहीहरुको संलग्नातामा बर्ष को कम्तीमा एक पटक सार्वजनिक सुनुवाई कार्यक्रम आयोजना गरेको, ', 
            'स्थानीय तहको आफ्नो क्षेत्रभित्रका कार्यक्रम सम्बन्धी सम्पूर्ण सूचना तथा जानकारी अध्यावधिक गरी नियमित रुपमा सार्वजनिक गरेको।', 
            'ज्याला तथा निर्वाह भत्ता बैङ्गिग प्रणालिबाट वितरण गरेको '
        ]

        # descriptions = TransparencyDetail.objects.filter(
        #     name__in=initial_service
        # )

        for description in initial_service:
            line = {
                'details': description
            }
            initial.append(line)
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = TransparencyDetailLineFormSet(
                self.request.POST, instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = TransparencyDetailLineFormSet(
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
        return reverse_lazy('transparency_detail:update', kwargs={'pk': self.object.pk})
