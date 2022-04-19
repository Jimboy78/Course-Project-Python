from django import forms

class Formulario_post(forms.Form):

    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    texto = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=50)