from django.contrib import admin

from core.models import (
    Client, Contact, Case
)


admin.site.register([
    Client,
    Contact,
    Case,
])