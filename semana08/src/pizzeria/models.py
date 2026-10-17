from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class DatosEntrega(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='datos_entrega',
    )
    direccion = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255, blank=True)
    instrucciones = models.TextField(blank=True)

    class Meta:
        ordering = ['direccion']

    def __str__(self):
        return f"Entrega de {self.cliente}"


class Ingrediente(models.Model):
    UNIDADES_MEDIDA = [
        ('gr', 'Gramos (gr)'),
        ('ml', 'Mililitros (ml)'),
        ('un', 'Unidades (un)'),
        ('kg', 'Kilogramos (kg)'),
        ('lt', 'Litros (lt)'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    unidad_medida = models.CharField(max_length=20, choices=UNIDADES_MEDIDA, default='gr')
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.get_unidad_medida_display()})"


class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Repartidor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    vehiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.vehiculo})"


class PizzaQuerySet(models.QuerySet):
    def disponibles(self):
        return self.filter(disponible=True)

    def con_receta(self):
        return self.select_related('categoria').prefetch_related('ingredientes')


class Pizza(models.Model):
    TIPO_MASA_CHOICES = [
        ('fina', 'Fina'),
        ('gruesa', 'Gruesa'),
        ('integral', 'Integral'),
    ]

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='pizzas',
    )
    nombre = models.CharField(max_length=100)
    tipo_masa = models.CharField(max_length=20, choices=TIPO_MASA_CHOICES)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    ingredientes = models.ManyToManyField(
        Ingrediente,
        through='RecetaPizza',
        related_name='pizzas',
    )

    objects = PizzaQuerySet.as_manager()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class PedidoQuerySet(models.QuerySet):
    def pendientes(self):
        return self.filter(estado='pendiente')

    def entregados(self):
        return self.filter(estado='entregado')

    def del_mes(self):
        hoy = timezone.now()
        return self.filter(fecha_pedido__year=hoy.year, fecha_pedido__month=hoy.month)

    def con_detalle(self):
        return self.select_related('cliente', 'cliente__datos_entrega', 'metodo_pago', 'repartidor').prefetch_related('detalles__pizza')


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En preparación'),
        ('en_camino', 'En camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    TIPO_PEDIDO_CHOICES = [
        ('presencial', 'Presencial'),
        ('delivery', 'Delivery'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    metodo_pago = models.ForeignKey(
        MetodoPago,
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    repartidor = models.ForeignKey(
        Repartidor,
        on_delete=models.PROTECT,
        related_name='pedidos',
        null=True,
        blank=True,
    )
    tipo_pedido = models.CharField(
        max_length=20,
        choices=TIPO_PEDIDO_CHOICES,
        default='presencial',
    )
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default='pendiente',
    )
    pizzas = models.ManyToManyField(
        Pizza,
        through='DetallePedido',
        related_name='pedidos',
    )

    objects = PedidoQuerySet.as_manager()

    class Meta:
        ordering = ['-fecha_pedido']

    def __str__(self):
        return f'Pedido #{self.pk} - {self.cliente}'


class RecetaPizza(models.Model):
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name='recetas',
    )
    ingrediente = models.ForeignKey(
        Ingrediente,
        on_delete=models.PROTECT,
        related_name='recetas',
    )
    cantidad_gramos = models.PositiveIntegerField(default=0)
    es_opcional = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pizza', 'ingrediente'],
                name='unique_receta_pizza',
            ),
        ]

    def __str__(self):
        return f'{self.pizza} - {self.ingrediente}'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles',
    )
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.PROTECT,
        related_name='detalles_pedido',
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pedido} - {self.pizza}'
