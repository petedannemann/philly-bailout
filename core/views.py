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
    CaseForm, ClientForm, ContactForm,
)


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'
    ordering = ['-updated_at']
    paginate_by = 5

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
    success_url = reverse_lazy('client-list')
    success_message = "%(name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(
            self.request, self.success_message % dict(
                name=obj.name,
            )
        )
        return super(ClientDeleteView, self).delete(request, *args, **kwargs)

class CaseCreateView(SuccessMessageMixin, CreateView):
    model = Case
    form_class = CaseForm
    success_message = "The case for %(name)s was created successfully."

    def get_context_data(self, **kwargs):
        context = super(CaseCreateView, self).get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        context['client'] = client
        return context

    def form_valid(self, form, **kwargs):
        case = form.save(commit=False)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        case.person = client
        return super(CaseCreateView, self).form_valid(form)

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
    success_message = "The case for %(name)s was updated successfully."

    def get_context_data(self, **kwargs):
        context = super(CaseUpdateView, self).get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        context['client'] = client
        return context

    def form_valid(self, form, **kwargs):
        case = form.save(commit=False)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        case.person = client
        return super(CaseUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.person.name,
        )

class CaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Case
    success_url = reverse_lazy('client-detail')
    success_message = "The case for %(first_name)s %(last_name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        person = self.get_object().person
        messages.success(self.request, self.success_message % person.__dict__)
        return super(CaseDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('client-detail', kwargs={'pk': self.object.person.pk})

class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_message = "The contact %(name)s was created successfully."

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        context['client'] = client
        return context

    def form_valid(self, form, **kwargs):
        case = form.save(commit=False)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        case.client = client
        return super(ContactCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

    def get_success_url(self):
        return reverse_lazy(
            'contact-detail', 
            kwargs={
                'client_id': self.object.client.id,
                'pk': self.object.pk
            }
        )

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(SuccessMessageMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    success_message = "The contact %(name)s was updated successfully."

    def get_context_data(self, **kwargs):
        context = super(ContactUpdateView, self).get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        context['client'] = client
        return context

    def form_valid(self, form, **kwargs):
        contact = form.save(commit=False)
        client_id = self.kwargs['client_id']
        client = Client.objects.get(pk=int(client_id))
        contact.person = client
        return super(ContactUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class ContactDeleteView(SuccessMessageMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')
    success_message = "The contact %(first_name)s %(last_name)s was deleted successfully."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ContactDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('client-detail', kwargs={'pk': self.object.client.pk})