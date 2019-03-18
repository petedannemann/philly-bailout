from django import forms

from core.models import Case, Client


class DateInput(forms.DateInput):
    '''Changing the input type makes this into a datepicker.'''
    input_type = 'date'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
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

class CaseSearchForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)