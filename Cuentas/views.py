from re import I
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import form_register, form_edit_user
from .models import NuestroUser


def Register (request): 
    if request.method == 'POST':
        form = form_register(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Indice/Plantillas/index.html", {'msj':f'Se creo el user {username}'})
        else:
            return render(request, "Cuentas/Plantillas/register.html", {'form':form})
    form = form_register()
    return render(request, "Cuentas/Plantillas/register.html", {'form':form})
  


def Login (request): 

    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                login(request, user)
                usuario = form.cleaned_data['username']
                return render(request, "Indice/Plantillas/index.html", {'msj':f'Bienvenido {usuario}!', 'user_avatar':Buscar_Url_Avatar(request.user)})
            else:
                return render(request, 'Cuentas/Plantillas/login.html', {'form':form})

        else:
            return render(request, 'Cuentas/Plantillas/login.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'Cuentas/Plantillas/login.html', {'form':form})




@login_required
def Editar (request):
    
    usuario_extendido, _ = NuestroUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = form_edit_user(request.POST,request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            logued_user = request.user 

            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name',)
            logued_user.last_name = data.get('last_name')
            usuario_extendido.imagen = data.get('imagen')
            usuario_extendido.link= data.get('link','')
            usuario_extendido.bio = data.get('biografia','')

 
            if data.get('password1') == data.get('password2') and len(data.get("password1")) >8:
                logued_user.set_password(data.get('password1'))
                msj = 'Se actualizo la contraseña' 
            else:
                msj = 'No se cambio la contraseña'

            logued_user.save()
            usuario_extendido.save()

            return render(request, "Indice/Plantillas/index.html", {'msj':msj, 'user_avatar':Buscar_Url_Avatar(request.user)})
        else:
            return render(request, "Cuentas/Plantillas/editar_user.html", {'form':form, 'msj':'', 'user_avatar':Buscar_Url_Avatar(request.user)})


    form = form_edit_user(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'imagen': usuario_extendido.imagen,
            'link': usuario_extendido.link,
            'bio': usuario_extendido.bio
        }
    )
    return render(request, "Cuentas/Plantillas/editar_user.html", {'form':form, 'msj':'', 'user_avatar':Buscar_Url_Avatar(request.user)})




def Buscar_Url_Avatar(user):
    return NuestroUser.objects.filter(user=user)[0].imagen.url
  