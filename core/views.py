from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy

from core.models import (
    Client, Case, Contact,
)
from core.forms import (
    CaseForm, ClientForm, CaseSearchForm,
)


class ClientCreateView(SuccessMessageMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_message = "%(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class ClientDetailView(DetailView):
    model = Client

class ClientUpdateView(SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_message = "%(name)s was updated successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class ClientDeleteView(SuccessMessageMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('cases-list')
    success_message = "%(name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ClientDeleteView, self).delete(request, *args, **kwargs)

class CaseListView(ListView):
    model = Case
    context_object_name = 'Cases'
    ordering = ['-updated_at']
    paginate_by = 5

class CaseCreateView(SuccessMessageMixin, CreateView):
    model = Case
    form_class = CaseForm
    success_message = "The case for %(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.person.name,
        )

class CaseDetailView(DetailView):
    model = Case

class CaseUpdateView(SuccessMessageMixin, UpdateView):
    model = Case
    form_class = CaseForm
    success_message = "The case for %(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.person.name,
        )

class CaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Case
    success_url = reverse_lazy('case-list')
    success_message = "The case for %(first_name)s %(last_name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        person = self.get_object().person
        messages.success(self.request, self.success_message % person.__dict__)
        return super(CaseDeleteView, self).delete(request, *args, **kwargs)

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        incarcerated_person = get_object_or_404(Client, pk=self.kwargs.get('pk'))
        return incarcerated_person.contacts

class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    fields = '__all__'
    success_message = "The contact %(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(SuccessMessageMixin, UpdateView):
    model = Contact
    fields = '__all__'
    success_message = "The contact %(name)s was updated successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class ContactDeleteView(SuccessMessageMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')
    success_message = "The contact %(name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ContactDeleteView, self).delete(request, *args, **kwargs)