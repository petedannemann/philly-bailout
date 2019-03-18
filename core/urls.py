from django.urls import path
from django.views.generic.base import TemplateView

from core.views import (
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    CaseCreateView,
    CaseDetailView,
    CaseUpdateView,
    CaseDeleteView,
    ContactCreateView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView,
)

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('client/<int:client_id>/case/new/', CaseCreateView.as_view(), name='case-create'),
    path('client/<int:client_id>/case/<int:case_id>/', CaseDetailView.as_view(), name='case-detail'),
    path('client/<int:client_id>/case/<int:case_id>/update/', CaseUpdateView.as_view(), name='case-update'),
    path('client/<int:client_id>/case/<int:case_id>/delete/', CaseDeleteView.as_view(), name='case-delete'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]