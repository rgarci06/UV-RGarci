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
    html = """<h1>Díes de la Setmana</h1>
    <h3>Per veure el dia de la semana posa un número del 1 al 7 al URL /número_del_dia</h3>
    <h4>ATENCIÓ: si poses un numero que sigui el 0 o menor et redirigirà a aquesta pàgina</h4>"""
    return HttpResponse(html)

def num(request, num:int):
    """Django no accepta paràmetres a les url's negatius, els fem a Strings
    i realitzem càsting per fer validacions (si no és numèric)
    """
    try:
        num=int(num)
    except ValueError:       
        return redirect("home")
        
    if num >=1 and num <=7:
        dies = {
            1: "Dilluns",
            2: "Dimarts",
            3: "Dimecres",
            4: "Dijous",
            5: "Divendres",
            6: "Dissabte",
            7: "Diumenge"
        }
        img = {
            1: "dilluns.jpg",
            2: "dimarts.jpg",
            3: "dimecres.jpg",
            4: "dijous.jpg",
            5: "divendres.jpg",
            6: "dissabte.jpg",
            7: "diumenge.jpg"
        }
        return HttpResponse(f"<h1>{dies[num]}</h1><img src='../media/{img[num]}' alt='Imatge {dies[num]}' size='400' height='400'>")

    if num > 7:
        html = """<h1>Valor numèric no permès</h1>"""
        return HttpResponseNotFound(html)

    if num <= 0:
        return redirect("home")
    
    return HttpResponse(f"<h1>{num}</h1>")
 


