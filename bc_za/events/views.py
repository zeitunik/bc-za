from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Nothing to see here, try logging in.")
