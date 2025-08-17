from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'title': 'Halaman Index',
        'menu' : 'home'
    }
    return render(request, 'data/main.html', context)

def Products(request):
    context = {
        'title': 'Halaman Products',
        'menu' : 'products'

    }
    return render(request, 'data/products.html', context)

def Custumer(request):
    context = {
        'title': 'Halaman Custumer',
        'menu' : 'custumer'

    }
    return render(request, 'data/custumer.html', context)
