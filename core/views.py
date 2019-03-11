from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from core.models import (
    IncarceratedPerson,
    Incarceration,
    Contact,
)
from core.forms import IncarcerationForm, IncarceratedPersonForm


class IncarceratedPersonCreateView(CreateView):
    model = IncarceratedPerson
    form_class = IncarceratedPersonForm

class IncarceratedPersonDetailView(DetailView):
    model = IncarceratedPerson

class IncarceratedPersonUpdateView(UpdateView):
    model = IncarceratedPerson
    form_class = IncarceratedPersonForm

class IncarceratedPersonDeleteView(DeleteView):
    model = IncarceratedPerson
    success_url = reverse_lazy('incarceratedperson-list')

class IncarcerationListView(ListView):
    model = Incarceration
    context_object_name = 'incarcerations'
    ordering = ['-updated_at']
    paginate_by = 5

class IncarcerationCreateView(CreateView):
    model = Incarceration
    form_class = IncarcerationForm

class IncarcerationDetailView(DetailView):
    model = Incarceration

class IncarcerationUpdateView(UpdateView):
    model = Incarceration
    form_class = IncarcerationForm

class IncarcerationDeleteView(DeleteView):
    model = Incarceration
    success_url = reverse_lazy('incarceration-list')

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        incarcerated_person = get_object_or_404(IncarceratedPerson, pk=self.kwargs.get('pk'))
        return incarcerated_person.contacts

class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')