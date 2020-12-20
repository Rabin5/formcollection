from django.core.exceptions import ValidationError
from django.forms import ModelForm

import nepali_datetime

from master_data.models import FiscalYear
from master_data.widgets import NepaliDateInput


class FyForm(ModelForm):
    class Meta:
        model = FiscalYear
        fields = ['name', 'date_start_bs', 'date_end_bs']
        widgets = {
            'date_start_bs': NepaliDateInput(),
            'date_end_bs': NepaliDateInput(),
        }
    
    def clean(self):
        """
        Overrides clean method to check if fiscal year is valid and unique.
        """

        is_clean = True
        cd = self.cleaned_data

        cd['date_start'] = nepali_datetime.datetime.strptime(cd.get('date_start_bs'), '%d/%m/%Y').date().to_datetime_date()
        cd['date_end'] = nepali_datetime.datetime.strptime(cd.get('date_end_bs'), '%d/%m/%Y').date().to_datetime_date()

        if (cd.get('date_start') >= cd.get('date_end')):
            is_clean = False

        fys = FiscalYear.objects.all().exclude(id=self.instance.id)

        for fy in fys:
            if (
                (cd.get('date_start') <= fy.date_end) and \
                    (fy.date_start <= cd.get('date_end'))
                ):
                is_clean = False
        
        if is_clean:
            return cd
        else:
            raise ValidationError('Fiscal Year is not valid or unique.', code='not_unique')
    

    def save(self, commit=True):
        fy = super().save(commit=False)
        fy.date_start = nepali_datetime.datetime.strptime(fy.date_start_bs, '%d/%m/%Y').date().to_datetime_date()
        fy.date_end = nepali_datetime.datetime.strptime(fy.date_end_bs, '%d/%m/%Y').date().to_datetime_date()
        fy.save()
        return fy