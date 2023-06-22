from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    #CASCADE: Elimina el producto si se elimina la categoria
    #PROTECT: No permite eliminar la categoria si hay productos asociados
    #RESTRICT: No permite eliminar la categoria a menos que hayamos eliminado todos los productos que se encuentran asociados
    #SET_NULL: Si se elimina la categoria, el campo categoria del producto se establece en NULL
    #SET_DEFAULT: Si se elimina la categoria, el campo categoria del producto se establece en el valor por defecto
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
)
    
    
    
    