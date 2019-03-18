from django.contrib import admin

from core.models import (
    Client, Contact, Charge, Facility, Case
)


admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Charge)
admin.site.register(Facility)
admin.site.register(Case)