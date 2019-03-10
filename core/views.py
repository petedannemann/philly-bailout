from django.shortcuts import render
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


class IncarceratedPersonListView(ListView):
    model = IncarceratedPerson
    context_object_name = 'incarcerated_persons'

class IncarceratedPersonCreateView(CreateView):
    model = IncarceratedPerson
    fields = '__all__'

class IncarceratedPersonDetailView(DetailView):
    model = IncarceratedPerson

class IncarceratedPersonUpdateView(UpdateView):
    model = IncarceratedPerson
    fields = '__all__'

class IncarceratedPersonDeleteView(DeleteView):
    model = IncarceratedPerson
    success_url = reverse_lazy('incarceratedperson-list')

class IncarcerationListView(ListView):
    model = Incarceration
    context_object_name = 'incarcerations'

class IncarcerationCreateView(CreateView):
    model = Incarceration
    fields = '__all__'

class IncarcerationDetailView(DetailView):
    model = Incarceration

class IncarcerationUpdateView(UpdateView):
    model = Incarceration
    fields = '__all__'

class IncarcerationDeleteView(DeleteView):
    model = Incarceration
    success_url = reverse_lazy('incarceration-list')

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'

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