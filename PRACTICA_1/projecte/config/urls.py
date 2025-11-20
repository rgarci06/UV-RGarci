
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #admin site
    path('admin/', admin.site.urls),
    #4) amb include diem l'urls de l'app que volem agafar
    path('first/', include('setmana.urls')),
    
    path('vistes/', include('vistes_templates.urls')),
    
]
