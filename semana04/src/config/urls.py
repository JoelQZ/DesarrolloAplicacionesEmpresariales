from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redireccionar_a_inicio(request):
    return redirect('inicio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redireccionar_a_inicio, name='root'),
    path('', include('canchas.urls')),
    path('', include('pizzeria.urls')),
]