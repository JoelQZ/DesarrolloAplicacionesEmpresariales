from django.db import models


class Pizza(models.Model):
    MASA_CHOICES = [
        ('Masa delgada', 'Masa delgada'),
        ('Masa tradicional', 'Masa tradicional'),
        ('Masa integral', 'Masa integral'),
        ('Masa artesanal', 'Masa artesanal'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_masa = models.CharField(max_length=50, choices=MASA_CHOICES)
    ingredientes = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'