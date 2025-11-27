from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect

def home(request): # Aqui faig la pàgina del home amb el seus missatges
    html = """<h1>Díes de la Setmana</h1>
    <h3>Per veure el dia de la semana posa un número del 1 al 7 al URL /número_del_dia</h3>
    <h4>ATENCIÓ: si poses un numero que sigui el 0 o menor et redirigirà a aquesta pàgina</h4>"""
    return HttpResponse(html) # Aqui retorno la pàgina home

def num(request, num: str): # Aqui faig la URL fent que li paso un numero str
    try: # Aqui convierto el número de str a int
        num = int(num)
    except ValueError: # 
        return redirect("home")

    if num <= 0: # Aqui faig que si el numero es 0 o menor et redirigirà a la pàgina home
        return redirect("home")

    if 1 <= num <= 7: # Aqui he fet que si el numero esta entre 1 i 7 executa el codi que el que fa es mostrar un dia de la setmana amb la seva imatge segons el número
        dies = {
            1: "Dilluns",
            2: "Dimarts",
            3: "Dimecres",
            4: "Dijous",
            5: "Divendres",
            6: "Dissabte",
            7: "Diumenge",
        }
        img = {
            1: "dilluns.jpg",
            2: "dimarts.jpg",
            3: "dimecres.jpg",
            4: "dijous.jpg",
            5: "divendres.jpg",
            6: "dissabte.jpg",
            7: "diumenge.jpg",
        }
        return HttpResponse( # Retorna la pàgina amb el dia i la imatge corresponent segons el número
            f"<h1>{dies[num]}</h1>"
            f"<img src='../media/{img[num]}' alt='Imatge {dies[num]}' size='400' height='400'>"
        )

    if num > 7: # Si el número es major que 7 retorna un missatge d'error
        html = "<h1>Valor numèric no permès</h1>"
        return HttpResponseNotFound(html)
        
    return redirect("home")
