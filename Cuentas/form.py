from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def file_size(value): # add this to some file where you can import it from
    limit = 4 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Imagen demasiado grande. El archivo no puede pesar as de  2 MB.')

class form_register(UserCreationForm):
    email = forms.EmailField (required=False)
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class form_edit_user(forms.Form):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput(), required=False)
    first_name = forms.CharField(label="Nombre", max_length=20, required=False)
    last_name = forms.CharField(label="Apellido", max_length=20)
    imagen = forms.ImageField(label="Avatar", required=False,validators=[file_size])
    bio = forms.CharField(label="Biografia", max_length=150, required=False, widget=forms.Textarea)
    link = forms.URLField(label="Link", required=False)




