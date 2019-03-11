from django import forms

from core.models import Incarceration, IncarceratedPerson


class DateInput(forms.DateInput):
    '''Changing the input type makes this into a datepicker.'''
    input_type = 'date'

class IncarcerationForm(forms.ModelForm):
    class Meta:
        model = Incarceration
        fields = '__all__'
        widgets = {
            'referral_date': DateInput(),
            'date_incarcerated': DateInput(),
            'date_bail_set': DateInput(),
            'date_of_jail_interview': DateInput(),
            'date_support_call_completed': DateInput(),
        }

class IncarceratedPersonForm(forms.ModelForm):
    class Meta:
        model = IncarceratedPerson
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }