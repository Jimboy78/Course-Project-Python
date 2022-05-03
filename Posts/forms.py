from django import forms
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Imagen demasiado grande. El archivo no puede pesar as de  2 MB.')

class Formulario_post(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    texto = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=50)
    imagen_post = forms.ImageField(required=False,validators=[file_size])

class Buscar_post(forms.Form):
    titulo = forms.CharField(max_length=20)