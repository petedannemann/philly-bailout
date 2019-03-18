from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from core.models import Case, Client, Contact


class DateInput(forms.DateInput):
    '''Changing the input type makes this into a datepicker.'''
    input_type = 'date'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        exclude = ('person',)
        widgets = {
            'referral_date': DateInput(),
            'date_incarcerated': DateInput(),
            'date_bail_set': DateInput(),
            'date_of_jail_interview': DateInput(),
            'date_support_call_completed': DateInput(),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }