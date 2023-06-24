from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Producto

# Create your views here.

#/productos


def index(request):
    # return HttpResponse("Hola Futuro Ingeniero Emanuel, No te rindas sigue adelante")
    # productos = Producto.objects.all().values() #Nos permite poder buscar absolutamente todos los registros que se encuentran dentro de la misma base de datos
    # productos = Producto.objects.filter(puntaje=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__gte=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__lt=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.filter(puntaje__gt=3) #Nos permite pasarle argumentos nombrados que van a permitir que nuestras consultas sean un poco mas complejas
    # productos = Producto.objects.get(id=1) #Nos permite buscar un elemento en particular
    # productos = Producto.objects.get(pk=1) #Nos permite buscar un elemento en particular
    # print(productos)
    # return JsonResponse(list(productos), safe=False)

    #Plantillas 
    # productos = Producto.objects.all()

    # return render(
    #     request, 
    #     'index.html', 
    #     context={'productos': productos,}    
    # )

    #Compartiendo plantilas
        # productos = Producto.objects.all()

        # return render(
        #      request, 
        #      'index1.html', 
        #      context={'productos': productos,}    
        #  )

    #Parametros urls
    productos = Producto.objects.all()

    return render(
        request, 
        'index.html', 
        context={'productos': productos,}    
    )

# def detalle(requests, producto_id):
#     # return HttpResponse(f"Este es el producto {producto_id}")
#     try:
#         producto = Producto.objects.get(id=producto_id)

#         return render(
#             requests, 
#             'detalle.html',
#             context={'producto': producto})
#     except Producto.DoesNotExist:
#         raise Http404()

#Otra manera de hacerlo
def detalle(requests, producto_id):   
        producto = get_object_or_404(Producto, id=producto_id)

        return render(
            requests, 
            'detalle.html',
            context={'producto': producto}
        )


def formulario(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductForm()
             

    return render(
         request,
         'producto_form.html',
         {'form': form}
    )
    
    
    
    
    