from django.forms import TextInput

import nepali_datetime


class NepaliDateInput(TextInput):
    template_name = 'widgets/nepali_datepicker.html'

    def format_value(self, value):
        """
        Return a value as it should appear when rendered in a template.
        """
        if not value:
            return ''
        elif type(value) == str:
            return value
        else:
            return nepali_datetime.date.from_datetime_date(value).strftime('%d/%m/%Y')