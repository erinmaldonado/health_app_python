from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for Health App."""
    return render(request, 'health_app/index.html')
