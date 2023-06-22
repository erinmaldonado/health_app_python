from django.shortcuts import render
from .models import Symptom


# Create your views here.
def index(request):
    """The home page for Health App."""
    return render(request, 'health_app/index.html')


def symptoms(request):
    """Show all symptoms"""
    symptoms = Symptom.objects.order_by('date_added')
    context = {'symptoms': symptoms}
    return render(request, 'health_app/symptoms.html', context)

