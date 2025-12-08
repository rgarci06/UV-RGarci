from django.shortcuts import render

personatges = {
    "Goku": {
        "nom": "Son Goku",
        "frase": "Lucharé para proteger a todos los que quiero.",
        "img": "/media/dragonball/goku.jpg",
        "opcio": "goku",
    },
    "Vegeta": {
        "nom": "Vegeta",
        "frase": "Soy el príncipe de los Saiyans, nunca me rendiré.",
        "img": "/media/dragonball/vegeta.jpg",
        "opcio": "vegeta",
    },
    "Gohan": {
        "nom": "Son Gohan",
        "frase": "Cuando mis amigos están en peligro, doy todo mi poder.",
        "img": "/media/dragonball/gohan.jpg",
        "opcio": "gohan",
    },
    "Piccolo": {
        "nom": "Piccolo",
        "frase": "Entrenar duro es la única forma de avanzar.",
        "img": "/media/dragonball/piccolo.jpg",
        "opcio": "piccolo",
    },
    "Krillin": {
        "nom": "Krillin",
        "frase": "Aunque caiga mil veces, siempre volveré a levantarme.",
        "img": "/media/dragonball/krilin.jpg",
        "opcio": "krillin",
    },
}


from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
        "mode": "home",
        "personatges": personatges.values(),
    })

def personatge(request, opcio):
    if opcio == "home":
        return home(request)

    personatge_trobat = None
    for p in personatges.values():
        if p["opcio"] == opcio:
            personatge_trobat = p
            break

    if personatge_trobat:
        return render(request, "home.html", {
            "mode": "informacio",
            "personatge": personatge_trobat,
        })

    return render(request, "home.html", {
        "mode": "error",
        "meme_url": "/media/dragonball/error.jpg",
        "missatge_error": "Aquest personatge no existeix.",
    })

