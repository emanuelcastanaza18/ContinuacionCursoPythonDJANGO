from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hola Futuro Ingeniero Emanuel, No te rindas sigue adelante")