from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def hoho(request):
    return render(request, 'hoho.html')


