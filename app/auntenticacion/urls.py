from django.urls import path

from .views import VistaRegistro, salir,acceder

# include to use the urls defined in the app blog specific in the file urls.py

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir")
]
