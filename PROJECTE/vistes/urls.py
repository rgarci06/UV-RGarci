'''
Fitxer que creem nosaltres per posar les vistes de l'app
'''
# per poder crear l'annex d'unió url=>view
from django.urls import path
from . import views

urlpatterns=[

# path=>serveix per definir una ruta (URL) 
# i indicar quina vista (view) s’ha d’executar quan algú hi accedeixi.
# nom funció
# name=>fixem nom per definir ruta i si fem canvi url només cal canviar-ho aquí

#'' indica arrel, el primer argument diu quin camí després del prefix de l’app activarà aquesta vista
  path('', views.home, name='home'),
  path('faqs', views.faqs, name='faqs'), 
  
#! recordar que el primer patró que coincideixi de les urls guanya per això es va dels més específics
#! als més genèrics   

# '<tipus_valor:paràmetre del view>'
  path('<str:num>', views.num, name='nombres'),

]