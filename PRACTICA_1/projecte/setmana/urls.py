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
  path('1', views.uno, name='uno'),
  path('2', views.dos, name='dos'),
  path('3', views.tres, name='tres'),
  path('4', views.quatre, name='quatre'),
  path('5', views.cinc, name='cinc'),
  path('6', views.sis, name='sis'),
  path('7', views.set, name='set'),
  
]