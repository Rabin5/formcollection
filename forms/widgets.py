from django.forms import Select


class ModelChoiceFieldSelect(Select):
    template_name = 'widgets/model_choice_field_with_create.html'