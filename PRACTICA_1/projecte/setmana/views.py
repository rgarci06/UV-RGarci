'''
A les vistes va tota la part de la lògica de programació, unió entre els templates i models.
Aquí retornarem HTML en cru, no cal dir-ho que no es pot fer, només és per mostrar-ho
'''

from django.http import HttpResponse, HttpResponseNotFound
# llibreria amb més funcionalitat actuals que funciona em processos interns
from django.shortcuts import redirect

# ? petició i resposta servidor -----------------------------------------------------------------------------

# definim una funció amb paràmetre request->petició al servidor
def home(request):
    
    # resposta servidor
    return HttpResponse ("<h1>Aquesta és el Home de la meva Web!</h1>")


def uno(request):
    return HttpResponse("<h1>Dilluns</h1>")

# ? request amb paràmetre url (dinamisme) i redirect -----------------------------------------------

def num(request, num:str):
    """Django no accepta paràmetres a les url's negatius, els fem a Strings
    i realitzem càsting per fer validacions (si no és numèric)
    """
    try:
        num=int(num)
    except ValueError:       
        # si volem redireccionar a una url utilitzem redirect(name de l'url, id=paràmetre a l'url) 
        return redirect("home")
    
    if num<0 or num>9:
        return HttpResponseNotFound("<h1>Paràmetre que no està dins del rang</h1>")
    
    return HttpResponse(f"<h1>{num}</h1>")
 


