from django.shortcuts import render

# Create your views here.
def professional(request):
    return render(request, 'professional/professional.html')