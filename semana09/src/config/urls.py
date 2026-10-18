from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redireccionar_a_inicio(request):
    return redirect('pizza_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redireccionar_a_inicio, name='root'),
    path('', include('pizzeria.urls')),
]