import datetime

from django import forms
from django.core.exceptions import ValidationError

import nepali_datetime

from forms.widgets import ModelChoiceFieldSelect
from master_data.widgets import NepaliDateInput


class ModelChoiceFieldWithCreate(forms.ModelChoiceField):
    """
    Works if new instance is to be created and only value of single field is provided for new instance
    """
    widget = ModelChoiceFieldSelect

    def __init__(self, queryset, *, empty_label="---------",
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, limit_choices_to=None,
                 blank=False, save_to_field='name', **kwargs):
        """
        @save_to_field: is added; for saving new value in that field
        """
        # Call Field instead of ChoiceField __init__() because we don't need
        # ChoiceField.__init__().
        forms.fields.Field.__init__(
            self, required=required, widget=widget, label=label,
            initial=initial, help_text=help_text, **kwargs
        )
        if (
            (required and initial is not None) or
            (isinstance(self.widget, forms.widgets.RadioSelect) and not blank)
        ):
            self.empty_label = None
        else:
            self.empty_label = empty_label
        self.queryset = queryset
        self.limit_choices_to = limit_choices_to   # limit the queryset later.
        self.to_field_name = to_field_name
        self.save_to_field = save_to_field
        

    def to_python(self, value):
        try:
            value = super().to_python(value)
            return value
        except ValidationError:
            params = {
                self.save_to_field: value
            }

            obj = self.queryset.model.objects.filter(**params)
            if obj:
                return obj[0]
            
            new_obj = self.queryset.model.objects.create(
                **params
            )
            return new_obj


class NepaliDateField(forms.DateField):
    widget = NepaliDateInput
    # range of date computed by nepali_datetime is 1918-4-13 to 2044-4-13
    min_date = datetime.date(1975, 1, 1)
    max_date = datetime.date(2100, 12, 30)
        
    
    def to_python(self, value):
        if value:
            try:
                date_str = datetime.datetime.strptime(value, '%d/%m/%Y').date()
            except:
                raise ValidationError('Invalid format. Please ensure this format is followed: dd/mm/yyyy')
            if date_str:
                if date_str > self.min_date and date_str < self.max_date:
                    value = nepali_datetime.datetime.strptime(value, '%d/%m/%Y').to_datetime_date()
                else:
                    raise ValidationError(f'Please enter date between {self.min_date} and {self.max_date} (BS).')

        return value
