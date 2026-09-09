from django.db import models
from pizza.models import Pizza


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Order(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordenes')
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT, related_name='ordenes')
    cantidad = models.IntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'