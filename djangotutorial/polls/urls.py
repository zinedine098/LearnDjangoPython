from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # /polls/ akan diarahkan ke views.index    
    path('products/', views.Products, name='products'),
    path('custumer/', views.Custumer, name='custumer'),
]
