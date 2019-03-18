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

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def cases(self):
        return Case.objects.filter(person=self.pk)

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

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})

class Contact(Person):
    email = models.EmailField(blank=False)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

class Charge(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # It would probably be useful to have address and facility contact information here

    def __str__(self):
        return self.name

class Case(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    referral_date = models.DateField(blank=False)
    referred_by = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False, related_name='referred_by')
    date_incarcerated = models.DateField()
    date_bail_set = models.DateField()
    date_of_jail_interview = models.DateField()
    bail_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, blank=False)
    docket_number = models.IntegerField()
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False, related_name='contact')
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
        return reverse('incarceration-detail', kwargs={'pk': self.pk})
