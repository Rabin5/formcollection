from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.db.models import query, F
from django.forms import inlineformset_factory
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from oagn_covid.settings import PAGINATED_BY

from forms import models

from collection.forms.covid_hospital_forms import CovHosFormCollectionForm
from collection.models import CovHosFormCollection
from collection.metadata import ROUTE_LINK
from collection.utils import CH_STATE, num_to_devanagari, find_empty_fields, filter_helper, date_filter, STATUS
from master_data.models import FiscalYear, Province, District, LocalLevel, CovidHospital

from users.models.user import User
from django.contrib.auth.models import Group

from django_weasyprint.views import WeasyTemplateView
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings
import os


# Convert utils CH_STATE to dict
DICT_CH_STATE = {key: value for key, value in CH_STATE}
dict_status = {key: value for key, value in STATUS}
LIST_CH_STATE = [value for key, value in CH_STATE]


class CovHosFormCollectionCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Creates form collection and initializes all forms in the collection
    """
    template_name = 'cov_hos_form_collection/create.html'
    form_class = CovHosFormCollectionForm
    permission_required = 'users.perm_cov_hos_form'

    def init_forms(self):
        """
        Initializes(creates) forms of the collection and links them to it.
        """

        col_update_params = {}
        fiscal_year = self.object.fiscal_year
        
        for form in LIST_CH_STATE:
            if ROUTE_LINK[form]['form_field'] in ['cov_hos_equipment', 'covid_hos_mainpower', 'cov_hos_management_checklist']:
                form_obj = ROUTE_LINK[form]['model'].objects.create(
                    create_user=self.request.user,
                )
            else:
                if ROUTE_LINK[form]['form_field'] == 'fund_receipt_expense':
                    form_obj = ROUTE_LINK[form]['model'].objects.create(
                        body=self.object.body,
                        fiscal_year=fiscal_year,
                        create_user=self.request.user,
                        fiscal_year_from=fiscal_year,
                        fiscal_year_to=fiscal_year
                    )
                else:
                    form_obj = ROUTE_LINK[form]['model'].objects.create(
                        body=self.object.body,
                        fiscal_year=fiscal_year,
                        create_user=self.request.user,
                    )
            col_update_params[ROUTE_LINK[form]['form_field']] = form_obj

        CovHosFormCollection.objects.filter(
            pk=self.object.pk).update(**col_update_params)
        return True

    def get(self, request, *args, **kwargs):
        """
        renders forms initial page to fill initial data like province, district
        """
        context = {}
        context['districts'] = list(District.objects.all().values('id', 'province_id', text=F('name')))
        context['local_levels'] = list(LocalLevel.objects.all().values('id', 'district_id', text=F('name')))
        context['hospitals'] = list(CovidHospital.objects.all().values('id', 'local_level_id', text=F('name')))
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
        form_url = f"{reverse('cov_hos_forms:cov_hos_update', kwargs={'pk': instance.pk})}?form={DICT_CH_STATE.get(0)}"
        return HttpResponseRedirect(form_url)


class CovHosFormCollectionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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
    model = CovHosFormCollection
    success_url = 'cov_hos_forms:cov_hos_list'
    form_class = ''
    route_link = ''
    form_field = None
    is_first_form = False
    is_last_form = False
    current_form_instance = None
    next_state = 'next'
    next_form = None
    permission_required = 'users.perm_cov_hos_form'

    def _get_cur_form_instance(self, pk):
        """
        returns instance of the current form
        """
        collection = CovHosFormCollection.objects.get(pk=pk)
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
            'percentage_completed_nepali': f'{num_to_devanagari(percentage)}%',
            'list_view_url': reverse('cov_hos_forms:cov_hos_list'),
        }

        return metadata

    def get(self, request, pk, *args, **kwargs):
        """
        Get and return form template response
        """
        self.object = CovHosFormCollection.objects.get(pk=pk)
        if not request.GET.get('form'):
            return HttpResponseRedirect(reverse('cov_hos_forms:cov_hos_update', kwargs={'pk': pk}) + f'?form={self.object.get_state_display()}')
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
                next_url = reverse('cov_hos_forms:cov_hos_update', kwargs={
                                   'pk': self.object.pk})+f'?form={self.next_form}'
            if self.is_last_form and self.next_state == 'submit':
                return HttpResponseRedirect(reverse_lazy(self.success_url))

            if self.next_state == 'review':
                return HttpResponseRedirect(reverse('cov_hos_forms:review', kwargs={
                                   'pk': self.object.pk, 'action': 'submit'}))
            return HttpResponseRedirect(next_url)
        else:
            return form_response

    def post(self, request, pk, *args, **kwargs):
        """
        Handle post request
        """
        self.object = CovHosFormCollection.objects.get(pk=pk)
        self.get_form_class(pk)

        context = {
            'metadata': self._get_metadata(),
            'collection_pk': pk,
            'collection': CovHosFormCollection.objects.get(pk=pk),
        }

        form_response = self.form_view.as_view(extra_context=context)(
            request, pk=self.current_form_instance.pk)
        return self._response(form_response)


class CovHosFormCollectionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CovHosFormCollection
    template_name = "cov_hos_form_collection/list.html"
    permission_required = 'users.perm_cov_hos_form'
    context_object_name = 'form_collections'
    paginate_by = PAGINATED_BY

    def get_queryset(self):
        province = self.request.GET.get('province', None)
        district = self.request.GET.get('district', None)
        local_level = self.request.GET.get('local_level', None)
        hospital = self.request.GET.get('hospital', None)
        fiscal_year = self.request.GET.get('fiscal_year', None)
        status = self.request.GET.get('status', None)
        
        form_collection = self.model.objects.filter(user=self.request.user)

        if province or district or local_level or hospital or fiscal_year or status:
            form_collection = filter_helper(form_collection, 
                        {'province_id': province, 'district_id': district, 'local_level_id': local_level, 'hospital_id': hospital, 'fiscal_year_id': fiscal_year, 'status':status}) 
        return form_collection


    def get_context_data(self, **kwargs):
        """
        renders forms initial page to fill initial data like province, district
        """
        context = super().get_context_data(**kwargs)
        context['provinces'] = list(Province.objects.all().values('id', text=F('name')))
        context['districts'] = list(District.objects.all().values('id', text=F('name')))
        context['local_levels'] = list(LocalLevel.objects.all().values('id', text=F('name')))
        context['hospitals'] = list(CovidHospital.objects.all().values('id', text=F('name')))
        context['fiscal_years'] = list(FiscalYear.objects.all().values('id', text=F('name')))
        context['statuses'] = dict_status
        return context


class CovHosFormCollectionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CovHosFormCollection
    template_name = "cov_hos_form_collection/delete.html"
    permission_required = 'users.perm_cov_hos_form'
    success_url = reverse_lazy('cov_hos_forms:cov_hos_list')
    context_object_name = 'form_collections'


class CovHosFormCollectionReview(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CovHosFormCollection
    template_name = "cov_hos_form_collection/review.html"
    permission_required = 'users.perm_cov_hos_form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'action' in self.kwargs:
            context['action'] = self.kwargs['action']
        context['empty_fields'] = find_empty_fields(self.object, 'cov_hos_forms', 'cov_hos_update', ROUTE_LINK, CH_STATE)
        return context

class CovHosFormCollectionReportPdf(WeasyTemplateResponseMixin, CovHosFormCollectionReview):
    model = CovHosFormCollection
    template_name = 'cov_hos_form_collection/report.html'
    pdf_filename = 'CovHosFormCollectionReport.pdf'
    pdf_stylesheets = [
        os.path.join(os.path.dirname(settings.BASE_DIR), 'static/styles', 'style.css'),
    ]


# class CovHosFormCollectionReportPdf(LoginRequiredMixin, PermissionRequiredMixin, WeasyTemplateView):
#     model = CovHosFormCollection
#     permission_required = 'users.perm_cov_hos_form'
#     ordering = ['-pk']
#     template_name = 'cov_hos_form_collection/report.html'
#     pdf_filename = 'CovHosFormCollectionReport.pdf'
#     pdf_stylesheets = [
#         os.path.join(os.path.dirname(settings.BASE_DIR), 'static', 'style.css'),
#     ]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     cov_hos = CovHosFormCollection.objects.filter(user=self.request.user).order_by('-id')
        
    #     context['cov_hos'] = cov_hos
        
    #     return context



@login_required
@permission_required('users.perm_cov_hos_form')
def cov_hos_submit_form(request, form_pk):
    form_obj = CovHosFormCollection.objects.get(id=form_pk)
    status = request.POST.get('status')
    form_obj.status = status
    form_obj.approver = request.user
    if 'reject_msg' in request.POST:
        form_obj.reject_msg = request.POST.get('reject_msg')
    form_obj.save()
    return JsonResponse({'success': '200'}, status=200)


class ApproveView(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'cov_hos_form_collection/approve.html'
    permission_required = 'users.perm_cov_hos_form_approve'

    def get(self, request, *args, **kwargs):
        context = []
        data = CovHosFormCollection.objects.select_related().filter(user=self.request.user, status__in=['submitted', 'approved', 'rejected'])

        province = self.request.GET.get('province', None)
        district = self.request.GET.get('district', None)
        local_level = self.request.GET.get('local_level', None)
        hospital = self.request.GET.get('hospital', None)
        fiscal_year = self.request.GET.get('fiscal_year', None)
        status = self.request.GET.get('status', None)

        if province or district or local_level or hospital or fiscal_year or status:
            data = filter_helper(data, 
                        {'province_id': province, 'district_id': district, 'local_level_id': local_level, 'hospital_id': hospital, 'fiscal_year_id': fiscal_year, 'status': status}) 

        for index, val in enumerate(data):
            context.append({'user':val.user, 'state': val.get_state_display(), 'id': val.id, 'status': val.get_status_display()})

        returnContext = {'data': context,
        'provinces':list(Province.objects.all().values('id', text=F('name'))),
        'fiscal_years':list(FiscalYear.objects.all().values('id', text=F('name'))),
        'districts':list(District.objects.all().values('id', text=F('name'))),
        'local_levels':list(LocalLevel.objects.all().values('id', text=F('name'))),
        'hospitals':list(CovidHospital.objects.all().values('id', text=F('name'))),
        'statuses': {'submitted':'SUBMITTED', 'approved':'APPROVED', 'rejected':'REJECTED'}
        }

        return render(request, self.template_name, context=returnContext)
