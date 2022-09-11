from django.shortcuts import render
from .models import Personal

# Create your views here.
def details(request):
    return render(request, 'details/details.html')

    data={
        'details':details
    }