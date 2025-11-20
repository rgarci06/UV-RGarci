from django.shortcuts import HttpResponse, redirect
from django.http import HttpResponseNotFound

#)2 Creem funció param:request que serà URL i return resposta servidor
def home(request):
    
    # HttpResponse és la resposta del servidor
    return HttpResponse("<h1>Home</h1>")


#? funció amb paràmetre url ---------------------------------------------------------------------

def parametre(request, nom:str):
    
    # paràmetre és el que posem url ha de tenir el mateix nom
    
    return HttpResponse(f"<h1>Hola {nom}!!!</h1>")

#? el funcionament del redirect ----------------------------------------------------------

def redirigir(request, nom:str):
    
    if not nom.isalpha():
        # retorna resposta errònia=>gestionar errors molt simples
        return HttpResponseNotFound("<h1>No pot haver-hi caràcters estranys a un nom!</h1>")

    if nom=="exit":
        # redireccionar el paramàtre és el name de l'url
        return redirect('home')
    
    return HttpResponse(f"<h1>Bon dia {nom}!!</h1>")

