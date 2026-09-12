from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),
    path('sedes/', views.sede_list, name='sede_list'),
    path('sedes/nueva/', views.sede_create, name='sede_create'),
    path('sedes/<int:pk>/editar/', views.sede_update, name='sede_update'),
    path('sedes/<int:pk>/eliminar/', views.sede_delete, name='sede_delete'),
    path('canchas/', views.cancha_list, name='cancha_list'),
    path('canchas/nueva/', views.cancha_create, name='cancha_create'),
    path('canchas/<int:pk>/editar/', views.cancha_update, name='cancha_update'),
    path('canchas/<int:pk>/eliminar/', views.cancha_delete, name='cancha_delete'),
    path('horarios/', views.horario_list, name='horario_list'),
    path('horarios/nuevo/', views.horario_create, name='horario_create'),
    path('horarios/<int:pk>/editar/', views.horario_update, name='horario_update'),
    path('horarios/<int:pk>/eliminar/', views.horario_delete, name='horario_delete'),
    path('reservas/', views.reserva_list, name='reserva_list'),
    path('reservas/nueva/', views.reserva_create, name='reserva_create'),
    path('reservas/<int:pk>/editar/', views.reserva_update, name='reserva_update'),
    path('reservas/<int:pk>/eliminar/', views.reserva_delete, name='reserva_delete'),
]