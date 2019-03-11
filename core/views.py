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
    IncarceratedPerson, Incarceration, Contact,
)
from core.forms import (
    IncarcerationForm, IncarceratedPersonForm, IncarcerationSearchForm,
)


class IncarceratedPersonCreateView(SuccessMessageMixin, CreateView):
    model = IncarceratedPerson
    form_class = IncarceratedPersonForm
    success_message = "%(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class IncarceratedPersonDetailView(DetailView):
    model = IncarceratedPerson

class IncarceratedPersonUpdateView(SuccessMessageMixin, UpdateView):
    model = IncarceratedPerson
    form_class = IncarceratedPersonForm
    success_message = "%(name)s was updated successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class IncarceratedPersonDeleteView(SuccessMessageMixin, DeleteView):
    model = IncarceratedPerson
    success_url = reverse_lazy('incarcerations-list')
    success_message = "%(name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(IncarceratedPersonDeleteView, self).delete(request, *args, **kwargs)

class IncarcerationListView(ListView):
    model = Incarceration
    context_object_name = 'incarcerations'
    ordering = ['-updated_at']
    paginate_by = 5

class IncarcerationCreateView(SuccessMessageMixin, CreateView):
    model = Incarceration
    form_class = IncarcerationForm
    success_message = "The incarceration for %(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.person.name,
        )

class IncarcerationDetailView(DetailView):
    model = Incarceration

class IncarcerationUpdateView(SuccessMessageMixin, UpdateView):
    model = Incarceration
    form_class = IncarcerationForm
    success_message = "The incarceration for %(name)s was created successfully."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.person.name,
        )

class IncarcerationDeleteView(SuccessMessageMixin, DeleteView):
    model = Incarceration
    success_url = reverse_lazy('incarceration-list')
    success_message = "The incarceration for %(first_name)s %(last_name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        person = self.get_object().person
        messages.success(self.request, self.success_message % person.__dict__)
        return super(IncarcerationDeleteView, self).delete(request, *args, **kwargs)

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        incarcerated_person = get_object_or_404(IncarceratedPerson, pk=self.kwargs.get('pk'))
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