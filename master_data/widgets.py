from django.forms import TextInput


class NepaliDateInput(TextInput):
    template_name = 'widgets/nepali_datepicker.html'