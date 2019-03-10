from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Person(models.Model):
    '''Abstract base class for making a person'''
    first_name = models.CharField(max_length=255, unique=False, blank=False)
    last_name = models.CharField(max_length=255, unique=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class IncarceratedPerson(Person):
    PRONOUN_CHOICES = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
        ('MISS', 'Miss'),
    )

    RACE_CHOICES = (
        ('AFRICAN-AMERICAN', 'African-American'),
        ('HISPANIC', 'Hispanic'),
        ('ASIAN', 'Asian'),
        ('CAUCASIAN', 'Caucasian'),
    )
    
    pronoun = models.CharField(max_length=4, choices=PRONOUN_CHOICES, blank=True)
    #TODO: Make this a multi-choice field with a plugin
    race = models.CharField(max_length=255, choices=RACE_CHOICES, blank=False) 
    date_of_birth = models.DateField(blank=True)
    open_to_speaking_to_the_press = models.BooleanField(default=False)
    ok_with_being_photographed = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('incarceratedperson-detail', kwargs={'pk': self.pk})

class Contact(Person):
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(blank=False)
    notes = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

class Charge(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    # It would probably be useful to have address and facility contact information here

    def __str__(self):
        return self.name

class Incarceration(models.Model):
    person = models.ForeignKey(IncarceratedPerson, on_delete=models.CASCADE, blank=False)
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
    notes = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.__class__.__name__}({self.person.name}, {self.date_incarcerated})'

    def get_absolute_url(self):
        return reverse('incarceration-detail', kwargs={'pk': self.pk})
