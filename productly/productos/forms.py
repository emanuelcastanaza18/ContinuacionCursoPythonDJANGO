from . import models
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
        