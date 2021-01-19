from django.db import transaction
from django.db.models import query
from django.forms import inlineformset_factory
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.views import View
from django.views.generic.edit import DeleteView
from forms import models
from forms.models import FormCollection
from django.apps import apps

from forms.metadata import ROUTE_LINK
from forms.utils import CH_STATE, num_to_devanagari
from master_data.models import FiscalYear

# Convert utils CH_STATE to dict
DICT_CH_STATE = {key:value for key, value in CH_STATE}
LIST_CH_STATE = [value for key, value in CH_STATE]

class FormCollectionCreateView(View):
    """
    Creates form collection and initializes all forms in the collection
    """

    def init_forms(self):
        """
        Initializes(creates) forms of the collection and links them to it.
        """

        col_update_params = {}
        fiscal_year = FiscalYear.objects.get_current_fy()
        for form in LIST_CH_STATE:
            form_obj = ROUTE_LINK[form]['model'].objects.create(
                body=self.request.user.body,
                fiscal_year=fiscal_year,
                create_user=self.request.user,
            )
            col_update_params[ROUTE_LINK[form]['form_field']] = form_obj
        
        FormCollection.objects.filter(pk=self.object.pk).update(**col_update_params)
        return True

    def post(self, request, *args, **kwargs):
        """
        Creates form collection and redirects to its update page
        """
        form_collect = FormCollection(user=request.user, status='started', state=0)
        form_collect.save()
        self.object = form_collect
        self.init_forms()
        form_url = f"{reverse('forms:update', kwargs={'pk': form_collect.pk})}?form={DICT_CH_STATE.get(0)}"
        context = {'url': form_url}
        return JsonResponse(context, content_type= 'application/json')
    

class FormCollectionUpdateView(UpdateView):
    """
    Contains added attributes:
        route_link => containing dict of form metadata from metadata.py
        form_field => routelink.form_field
        is_first_form => True if first form in collection
        is_last_form => True if last form in collection
        current_form_instance => instance of the current form in request
        next_state => determines what to render next;
            next: render next page in state
            previous: render previous page in state
            submit: submit form collection
        next_form: form to return and render next; determined by next_state
    """
    model = FormCollection
    success_url = 'forms:list'
    form_class = ''
    route_link = ''
    form_field = None
    is_first_form = False
    is_last_form = False
    current_form_instance = None
    next_state = 'next'
    next_form = None

    def _get_cur_form_instance(self, pk):
        """
        returns instance of the current form
        """
        collection = FormCollection.objects.get(pk=pk)
        return getattr(collection, self.form_field)

    def get_form_class(self, pk):
        '''
        Sets various attributes of the form collection and form
        Returns current form_class
        '''
        form = self.request.GET.get('form')

        self.current_form = form
        self.route_link = ROUTE_LINK.get(form)
        self.form_class = self.route_link['form']
        self.model = self.route_link['model']
        self.template_name = self.route_link['update_view'].template_name
        self.form_view = self.route_link['update_view']
        self.form_field = self.route_link['form_field']
        self.current_form_instance = self._get_cur_form_instance(pk)
        self.next_state = self.request.POST.get('next_state', 'next')
        return self.form_class
    
    def _get_metadata(self):
        """
        Returns metadata used in rendering form page of collection
        """
        total_forms = len(LIST_CH_STATE)
        if self.object.status in ('started', 'incomplete'):
            current_form = LIST_CH_STATE.index(self.current_form)
        else:
            current_form = total_forms
        percentage = int(current_form / total_forms * 100)

        if self.current_form == LIST_CH_STATE[0]:
            self.is_first_form = True
        
        if self.current_form == LIST_CH_STATE[-1]:
            self.is_last_form = True

        metadata = {
            'is_last_form': self.is_last_form,
            'is_first_form': self.is_first_form,
            'total_forms_nepali': num_to_devanagari(total_forms),
            'current_form_nepali': num_to_devanagari(current_form),
            'percentage_completed': f'{percentage}%',
            'percentage_completed_nepali': f'{num_to_devanagari(percentage)}%'
        }

        return metadata
    
    def get(self, request, pk, *args, **kwargs):
        """
        Get and return form template response
        """
        self.object = FormCollection.objects.get(pk=pk)
        if not request.GET.get('form'):
            return HttpResponseRedirect(reverse('forms:update', kwargs={'pk': pk}) + f'?form={self.object.get_state_display()}')
        self.get_form_class(pk)
        context = {
            'metadata': self._get_metadata(),
            'collection_pk': pk,
        }
        response = self.form_view.as_view(extra_context=context)(request, pk=self.current_form_instance.pk)
        
        return response
    
    def _get_state(self):
        """
        set next_form attribute
        return next state of form collection
        """
        current_state = LIST_CH_STATE.index(self.current_form)
        if self.next_state == 'previous':
            delta_idx = -1  # step for next form index
        else:
            delta_idx = 1
        next_state = current_state + delta_idx
        self.next_form = DICT_CH_STATE.get(next_state)
        if next_state > len(LIST_CH_STATE)-1:
            next_state = len(LIST_CH_STATE) - 1
        elif next_state < 0:
            next_state = 0
        
        return next_state
    
    def _update(self):
        """
        Update Form Collection object
        """
        self.object.status = 'submitted' if self.next_state == 'submit' else 'incomplete'
        self.object.state = self._get_state()
        self.object.save()

    def _response(self, form_response):
        """
        Update collection object and return appropriate response
        """
        if form_response.status_code == 302:
            self._update()
            if self.next_form:
                next_url = reverse('forms:update', kwargs={'pk': self.object.pk})+f'?form={self.next_form}'
            if self.is_last_form and self.next_state == 'submit':
                return HttpResponseRedirect(reverse_lazy(self.success_url))

            return HttpResponseRedirect(next_url)
        else:
            return form_response

    def post(self, request, pk, *args, **kwargs):
        """
        Handle post request
        """
        self.object = FormCollection.objects.get(pk=pk)
        self.get_form_class(pk)

        context = {
            'metadata': self._get_metadata(),
            'collection_pk': pk,
            'collection': FormCollection.objects.get(pk=pk),
        }

        form_response = self.form_view.as_view(extra_context=context)(request, pk=self.current_form_instance.pk)
        return self._response(form_response)


class FormCollectionListView(ListView):
    model = FormCollection
    template_name = "forms/form_collection/list.html"
    context_object_name = 'form_collections'

class FormCollectionDeleteView(DeleteView):
    pass
