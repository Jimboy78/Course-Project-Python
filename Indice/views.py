from django.shortcuts import render

# Create your views here.
    
def Inicio (request): 

    return render(request, "index.html", {})

def AboutUs (request): 

    return render(request, "about_us.html", {})
def Blog (request): 

    return render(request, "blog.html", {})
def Register (request): 

    return render(request, "register.html", {})
def Login (request): 

    return render(request, "login.html", {})
