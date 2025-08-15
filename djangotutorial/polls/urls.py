from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /polls/ akan diarahkan ke views.index
]
