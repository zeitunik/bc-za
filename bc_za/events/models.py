"""Models for the Events app."""

from django.db import models


class Event(models.Model):
    """Event model class."""

    name = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=255)
    max_number_participants = models.IntegerField(verbose_name="maximum number of participants")
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Represent the event as a string."""
        return str(self.name)
