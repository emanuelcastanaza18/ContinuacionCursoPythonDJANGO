from django.contrib import admin
from .models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'puntaje', 'creado_en')



# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
