from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.db.models import query, F
from django.forms import inlineformset_factory
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.views import View
from django.views.generic.edit import DeleteView
from forms import models
from django.contrib.auth.models import Group


from django.apps import apps

from collection.forms.local_level_forms import LocalLevelFormCollectionForm
from collection.models import LocalLevelFormCollection
from collection.metadata import ROUTE_LINK
from collection.utils import LOCAL_LEVEL_STATE, num_to_devanagari, find_empty_fields

from master_data.models import FiscalYear, District, LocalLevel
from oagn_covid.settings import PAGINATED_BY
from django.contrib.auth.decorators import login_required, permission_required

# Convert utils LOCAL_LEVEL_STATE to dict
DICT_LOCAL_LEVEL_STATE = {key: value for key, value in LOCAL_LEVEL_STATE}
LIST_LOCAL_LEVEL_STATE = [value for key, value in LOCAL_LEVEL_STATE]


class LocalLevelFormCollectionCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Creates form collection and initializes all forms in the collection
    """
    form_class = LocalLevelFormCollectionForm
    template_name = 'local_level_form_collection/create.html'
    permission_required = 'users.perm_local_level_form'

    def init_forms(self):
        """
        Initializes(creates) forms of the collection and links them to it.
        """

        col_update_params = {}
        fiscal_year = self.object.fiscal_year
        for form in LIST_LOCAL_LEVEL_STATE:
            if ROUTE_LINK[form]['form_field'] in ['cov_hos_equipment', 'covid_hos_mainpower']:
                form_obj = ROUTE_LINK[form]['model'].objects.create(
                    create_user=self.request.user,
                )
            elif ROUTE_LINK[form]['form_field'] in ['action_plan_implementation']:
                form_obj = ROUTE_LINK[form]['model'].objects.create(
                    body=self.object.body,
                    create_user=self.request.user,
                )
            else:
                form_obj = ROUTE_LINK[form]['model'].objects.create(
                    body=self.object.body,
                    fiscal_year=fiscal_year,
                    create_user=self.request.user,
                )
            col_update_params[ROUTE_LINK[form]['form_field']] = form_obj

        LocalLevelFormCollection.objects.filter(
            pk=self.object.pk).update(**col_update_params)
        return True
    
    def get(self, request, *args, **kwargs):
        """
        renders forms initial page to fill initial data like province, district
        """
        context = {}
        context['districts'] = list(District.objects.all().values('id', 'province_id', text=F('name')))
        context['local_levels'] = list(LocalLevel.objects.all().values('id', 'district_id', text=F('name')))
        context['form'] = self.form_class()
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        """
        Creates form collection and redirects to its update page
        """
        form_collect = self.form_class(request.POST)
        instance = form_collect.save()
        instance.user = request.user
        instance.status = 'started'
        instance.state = 0
        instance.save()
        self.object = instance
        self.init_forms()
        form_url = f"{reverse('local_level_forms:local_level_update', kwargs={'pk': self.object.pk})}?form={DICT_LOCAL_LEVEL_STATE.get(0)}"
        return HttpResponseRedirect(form_url)


class LocalLevelFormCollectionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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
    model = LocalLevelFormCollection
    success_url = 'local_level_forms:local_level_list'
    form_class = ''
    route_link = ''
    form_field = None
    is_first_form = False
    is_last_form = False
    current_form_instance = None
    next_state = 'next'
    next_form = None
    permission_required = 'users.perm_local_level_form'

    def _get_cur_form_instance(self, pk):
        """
        returns instance of the current form
        """
        collection = LocalLevelFormCollection.objects.get(pk=pk)
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
        total_forms = len(LIST_LOCAL_LEVEL_STATE)
        if self.object.status in ('started', 'incomplete'):
            current_form = LIST_LOCAL_LEVEL_STATE.index(self.current_form)
        else:
            current_form = total_forms
        percentage = int(current_form / total_forms * 100)

        if self.current_form == LIST_LOCAL_LEVEL_STATE[0]:
            self.is_first_form = True

        if self.current_form == LIST_LOCAL_LEVEL_STATE[-1]:
            self.is_last_form = True

        metadata = {
            'is_last_form': self.is_last_form,
            'is_first_form': self.is_first_form,
            'total_forms_nepali': num_to_devanagari(total_forms),
            'current_form_nepali': num_to_devanagari(current_form),
            'percentage_completed': f'{percentage}%',
            'percentage_completed_nepali': f'{num_to_devanagari(percentage)}%',
            'list_view_url': reverse('local_level_forms:local_level_list'),
        }

        return metadata

    def get(self, request, pk, *args, **kwargs):
        """
        Get and return form template response
        """
        self.object = LocalLevelFormCollection.objects.get(pk=pk)
        if not request.GET.get('form'):
            return HttpResponseRedirect(reverse('local_level_forms:local_level_update', kwargs={'pk': pk}) + f'?form={self.object.get_state_display()}')
        self.get_form_class(pk)
        context = {
            'metadata': self._get_metadata(),
            'collection_pk': pk,
        }
        response = self.form_view.as_view(extra_context=context)(
            request, pk=self.current_form_instance.pk)

        return response

    def _get_state(self):
        """
        set next_form attribute
        return next state of form collection
        """
        current_state = LIST_LOCAL_LEVEL_STATE.index(self.current_form)
        if self.next_state == 'previous':
            delta_idx = -1  # step for next form index
        else:
            delta_idx = 1
        next_state = current_state + delta_idx
        self.next_form = DICT_LOCAL_LEVEL_STATE.get(next_state)
        if next_state > len(LIST_LOCAL_LEVEL_STATE)-1:
            next_state = len(LIST_LOCAL_LEVEL_STATE) - 1
        elif next_state < 0:
            next_state = 0

        return next_state

    def _update(self):
        """
        Update Form Collection object
        """
        self.object.status = 'submitted' if self.next_state == 'submit' else 'incomplete'
        self.object.state = self._get_state()
        if self.object.reject_msg:
            self.object.reject_msg = ''
            self.object.approver = None
        self.object.save()

    def _response(self, form_response):
        """
        Update collection object and return appropriate response
        """
        if form_response.status_code == 302:
            self._update()
            if self.next_form:
                next_url = reverse('local_level_forms:local_level_update', kwargs={
                                   'pk': self.object.pk})+f'?form={self.next_form}'
            if self.is_last_form and self.next_state == 'submit':
                return HttpResponseRedirect(reverse_lazy(self.success_url))

            if self.next_state == 'review':
                return HttpResponseRedirect(reverse('local_level_forms:review', kwargs={
                                    'pk': self.object.pk, 'action': 'submit'}))

            return HttpResponseRedirect(next_url)
        else:
            return form_response

    def post(self, request, pk, *args, **kwargs):
        """
        Handle post request
        """
        self.object = LocalLevelFormCollection.objects.get(pk=pk)
        self.get_form_class(pk)

        context = {
            'metadata': self._get_metadata(),
            'collection_pk': pk,
            'collection': LocalLevelFormCollection.objects.get(pk=pk),
        }

        form_response = self.form_view.as_view(extra_context=context)(
            request, pk=self.current_form_instance.pk)
        return self._response(form_response)


class LocalLevelFormCollectionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LocalLevelFormCollection
    template_name = "local_level_form_collection/list.html"
    permission_required = 'users.perm_local_level_form'
    context_object_name = 'form_collections'
    paginate_by = PAGINATED_BY


class LocalLevelFormCollectionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = LocalLevelFormCollection
    template_name = "local_level_form_collection/delete.html"
    permission_required = 'users.perm_local_level_form'
    success_url = reverse_lazy('local_level_forms:local_level_list')
    context_object_name = 'form_collections'


class LocalLevelFormCollectionReviewView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = LocalLevelFormCollection
    template_name = "local_level_form_collection/review.html"
    permission_required = 'users.perm_local_level_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = self.kwargs['action']
        context['empty_fields'] = find_empty_fields(self.object, 'local_level_forms', 'local_level_update', ROUTE_LINK, LOCAL_LEVEL_STATE)
        return context

@login_required
@permission_required('users.perm_local_level_form')
def local_level_submit_form(request, form_pk):
    form_obj = LocalLevelFormCollection.objects.get(id=form_pk)
    status = request.POST.get('status')
    form_obj.status = status
    form_obj.approver = request.user
    if 'reject_msg' in request.POST:
        form_obj.reject_msg = request.POST.get('reject_msg')
    form_obj.save()
    return JsonResponse({'success': '200'}, status=200)

class ApproveView(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'local_level_form_collection/approve.html'
    permission_required = 'users.perm_local_level_form_approve'

    def get(self, request, *args, **kwargs):
        context = []
        data = list(LocalLevelFormCollection.objects.select_related().filter(status__in=['submitted', 'approved', 'rejected']))
        print(data)
        for index, val in enumerate(data):
            context.append({'user':val.user, 'state': val.get_state_display(), 'id': val.id, 'status': val.get_status_display()})
        return render(request, self.template_name, context={'data': context})