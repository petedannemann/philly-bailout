from django.contrib import admin

from core.models import (
    IncarceratedPerson, Contact, Charge, Facility, Incarceration
)


admin.site.register(IncarceratedPerson)
admin.site.register(Contact)
admin.site.register(Charge)
admin.site.register(Facility)
admin.site.register(Incarceration)