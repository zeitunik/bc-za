from django.shortcuts import get_object_or_404, render

from .models import Event


def index(request):
    upcoming_events = Event.objects.order_by("start")[:5]
    context = {"upcoming_events": upcoming_events}
    return render(request, "events/index.html", context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/detail.html", {"event": event})
