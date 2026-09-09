from django.contrib import admin
from .models import Cliente, Sede, Cancha, Horario, Reserva

admin.site.register(Cliente)
admin.site.register(Sede)
admin.site.register(Cancha)
admin.site.register(Horario)
admin.site.register(Reserva)