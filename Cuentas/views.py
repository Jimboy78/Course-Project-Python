from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .form import form_register


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
                return render(request, "Indice/Plantillas/index.html", {'msj':'Te re logeaste'})
            else:
                return render(request, 'Cuentas/Plantillas/login.html', {'form':form})

        else:
            return render(request, 'Cuentas/Plantillas/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'Cuentas/Plantillas/login.html', {'form':form})
