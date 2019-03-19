from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from multiselectfield import MultiSelectField


class Person(models.Model):
    '''Abstract base class for making a person.'''
    first_name = models.CharField(max_length=255, unique=False, blank=False)
    last_name = models.CharField(max_length=255, unique=False, blank=False)
    phone_number = models.CharField(max_length=25, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name

class Client(Person):
    PRONOUN_CHOICES = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
        ('MISS', 'Miss'),
    )

    RACE_CHOICES = (
        ('AFRICAN AMERICAN', 'African American'),
        ('AMERICAN INDIAN', 'American Indian'),
        ('ASIAN', 'Asian'),
        ('HISPANIC OR LATINO', 'Hispanic or Latino'),
        ('NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER', 'Native Hawaiian or Other Pacific Islander'),
        ('WHITE', 'White'),
    )
    
    pronoun = models.CharField(max_length=4, choices=PRONOUN_CHOICES, blank=True)
    race = MultiSelectField(choices=RACE_CHOICES, blank=False) 
    date_of_birth = models.DateField(blank=True)
    open_to_speaking_to_the_press = models.BooleanField(default=False)
    ok_with_being_photographed = models.BooleanField(default=False)

    @property
    def cases(self):
        return Case.objects.filter(person=self.pk)

    @property
    def contacts(self):
        return Contact.objects.filter(client=self.pk)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})

class Case(models.Model):
    FACILITY_CHOICES = (
        ('CURRAN FROMHOLD CORRECTIONAL FACILITY', 'Curran-Fromhold Correctional Facility'),
        ('CORRECTIONS DEPARTMENT', 'Corrections Department'),
        ('JUVENILE JUSTICE SERVICES CENTER', 'Juvenile Justice Services Center'),
        ('PHILADELPHIA INDUSTRIAL CORRECTIONAL CENTER', 'Philadelphia Industrial Correctional Center'),
    )

    CHARGE_CHOICES = (
        ('ASSAULT / BATTERY', 'Assault / Battery'),
        ('BURGLARY', 'Burglary'),
        ('BRIBERY', 'Bribery'),
        ('DRUG POSSESSION', 'Drug Possession'),
        ('THEFT / LARCENY', 'Theft / Larceny'),
    )

    person = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    referral_date = models.DateField(blank=False)
    referred_by = models.CharField(max_length=255, blank=True)
    date_incarcerated = models.DateField()
    date_bail_set = models.DateField()
    date_of_jail_interview = models.DateField()
    charges = MultiSelectField(choices=CHARGE_CHOICES, blank=False) 
    bail_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    facility = models.CharField(max_length=255, choices=FACILITY_CHOICES, blank=False)
    docket_number = models.IntegerField()
    support_caller = models.ForeignKey(User, on_delete=models.CASCADE)
    date_support_call_completed = models.DateField()
    support_funding_source = models.CharField(max_length=255, blank=True)
    opt_in_for_additional_resources = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='documents/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.__class__.__name__}({self.person.name}, {self.date_incarcerated})'

    def get_absolute_url(self):
        return reverse('case-detail', kwargs={'client_id': self.person.pk, 'pk': self.pk})

class Contact(Person):
    email = models.EmailField(blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'client_id': self.client.pk, 'pk': self.pk})