from forms.forms.cov_hos_equipment_forms import CovidHospitalEquipmentForm
from forms.forms.med_purchase_desc_forms import MedPurchaseDescForm
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm
from forms.forms.pcr_kit_usage_forms import PcrKitUsageForm

from forms import models

from forms.views import (
    cov_hos_equipment_views,
    med_purchase_desc_views,
    pcr_kit_usage_views,
    pcr_lab_detail_views
)

# Asign form, model, form collection field to route view name
"""
ROUTE_LINK is a dictionary containing form metadata used for all form collections.
"""
ROUTE_LINK = {
    'med_purchase_desc': {
        'title': 'केही प्रमुख स्वास्थ्य सामाग्रीको खरिद दर सम्बन्धी बिबरण (२०७६।७७)',
        'form': MedPurchaseDescForm,
        'model': models.MedicalPurchaseDescription,
        'form_field': 'med_purchase_desc',
        'update_view': med_purchase_desc_views.MedPurchaseDescUpdateView,
    },

    'pcr_lab_detail': {
        'title': 'पिसीआर प्रयोगशाला  सम्बन्धी बिबरण',
        'form': PcrLaboratoryDetailForm,
        'model': models.PcrLaboratoryDetail,
        'form_field': 'pcr_lab_detail',
        'update_view': pcr_lab_detail_views.PcrLaboratoryDetailUpdateView,
    },

    'pcr_kit_usage': {
        'title': 'पिसीआर किटको उपयोग सम्बन्धी बिबरण',
        'form': PcrKitUsageForm,
        'model': models.PcrKitUsage,
        'form_field': 'pcr_kit_usage',
        'update_view': pcr_kit_usage_views.PcrKitUsageUpdateView,
    },

    'cov_hos_equipment': {
        'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य उपकरण सम्बन्धी विवरण',
        'form': CovidHospitalEquipmentForm,
        'model': models.CovidHospitalEquipment,
        'form_field': 'cov_hos_equipment',
        'update_view': cov_hos_equipment_views.CovidHospitalEquipmentUpdateView,
    },
}
