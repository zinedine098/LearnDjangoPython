from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'title': 'Halaman Index',
    }
    return render(request, 'data/main.html', context)

def Products(request):
    context = {
        'title': 'Halaman Products',
    }
    return render(request, 'data/products.html', context)

def Custumer(request):
    context = {
        'title': 'Halaman Custumer',
    }
    return render(request, 'data/custumer.html', context)
