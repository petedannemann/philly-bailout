from django.urls import path
from django.views.generic.base import TemplateView

from core.views import (
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    CaseListView,
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
    path('', CaseListView.as_view(), name='case-list'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('case/new/', CaseCreateView.as_view(), name='case-create'),
    path('case/<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    path('case/<int:pk>/update/', CaseUpdateView.as_view(), name='case-update'),
    path('case/<int:pk>/delete/', CaseDeleteView.as_view(), name='case-delete'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]