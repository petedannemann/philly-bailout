from django.urls import path
from django.views.generic.base import TemplateView

from core.views import (
    IncarceratedPersonListView,
    IncarceratedPersonCreateView,
    IncarceratedPersonDetailView,
    IncarceratedPersonUpdateView,
    IncarceratedPersonDeleteView,
    IncarcerationListView,
    IncarcerationCreateView,
    IncarcerationDetailView,
    IncarcerationUpdateView,
    IncarcerationDeleteView,
    ContactListView,
    ContactCreateView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView,
)
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('incarceratedperson/', IncarceratedPersonListView.as_view(), name='incarceratedperson-list'),
    path('incarceratedperson/new/', IncarceratedPersonCreateView.as_view(), name='incarceratedperson-create'),
    path('incarceratedperson/<int:pk>/', IncarceratedPersonDetailView.as_view(), name='incarceratedperson-detail'),
    path('incarceratedperson/<int:pk>/update/', IncarceratedPersonUpdateView.as_view(), name='incarceratedperson-update'),
    path('incarceratedperson/<int:pk>/delete/', IncarceratedPersonDeleteView.as_view(), name='incarceratedperson-delete'),
    path('incarceration/', IncarcerationListView.as_view(), name='incarceration-list'),
    path('incarceration/new/', IncarcerationCreateView.as_view(), name='incarceration-create'),
    path('incarceration/<int:pk>/', IncarcerationDetailView.as_view(), name='incarceration-detail'),
    path('incarceration/<int:pk>/update/', IncarcerationUpdateView.as_view(), name='incarceration-update'),
    path('incarceration/<int:pk>/delete/', IncarcerationDeleteView.as_view(), name='incarceration-delete'),
    path('contact/', ContactListView.as_view(), name='contact-list'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]