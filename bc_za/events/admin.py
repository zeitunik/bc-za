"""Admin page setup."""

from django.contrib import admin

from .models import Event

admin.site.register(Event)
