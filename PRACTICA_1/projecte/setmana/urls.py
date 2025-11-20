from django.urls import path
# 3) importem vistes per unir url amb que vols que et mostri
from . import views

# gestió urls del més concret al genèric ja que llegeix de dalt a baix els urlspatterns

urlpatterns = [
    
    # url app, importem funció, name nom de referència a la ruta més fàcil de gestionar per canvis
    path("home", views.home, name="home"),
    
    # str, int, float...vigilar Django i els nombres negatius que no ho gestiona bé!!!
    path("param/<str:nom>", views.parametre, name="param"),
 
    path("redirect/<str:nom>", views.redirigir, name="redirect"),
    
]
