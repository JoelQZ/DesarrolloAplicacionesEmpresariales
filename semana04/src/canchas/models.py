from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Cancha(models.Model):
    TIPO_CHOICES = [
        ('futbol', 'Fulbito'),
        ('voley', 'Vóley'),
        ('tenis', 'Tenis'),
    ]
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    precio_hora = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Horario(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cancha} - {self.fecha} {self.hora_inicio}"


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva de {self.cliente} - {self.horario}"