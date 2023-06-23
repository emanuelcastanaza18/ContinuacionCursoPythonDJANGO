from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.

#/productos


def index(request):
    # return HttpResponse("Hola Futuro Ingeniero Emanuel, No te rindas sigue adelante")
    productos = Producto.objects.all().values() #Nos permite poder buscar absolutamente todos los registros que se encuentran dentro de la misma base de datos
    # productos = Producto.objects.filter(puntaje=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__gte=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__lt=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__gt=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.get(id=1) #Nos permite buscar un elemento en particular
    # productos = Producto.objects.get(pk=1) #Nos permite buscar un elemento en particular
    # print(productos)
    return JsonResponse(list(productos), safe=False)
