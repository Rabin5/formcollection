from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    template_name = 'reports/dashboard.html'
    