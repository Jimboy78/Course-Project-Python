from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import form_register


def Inicio (request): 
    return render(request, "index.html", {})


def AboutUs (request): 
    return render(request, "about_us.html", {})


def Blog (request): 
    return render(request, "blog.html", {})


def Register (request): 
    if request.method == 'POST':
        form = form_register(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {'msj':f'Se creo el user {username}'})
        else:
            return render(request, "register.html", {'form':form})
    form = form_register()
    return render(request, "register.html", {'form':form})
     



def Login (request): 

    if request.method == 'POST':   
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                login(request, user)
                return render(request, "index.html", {'msj':'Te re logeaste'})
            else:
                return render(request, 'login.html', {'form':form})

        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
