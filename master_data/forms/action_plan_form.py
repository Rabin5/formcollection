from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import ActionPlanActivity

class ActionPlanActivityForm(ModelForm):
    class Meta:
        model = ActionPlanActivity
        fields = '__all__'
