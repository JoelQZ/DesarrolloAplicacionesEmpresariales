#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pizza.models import Pizza
from order.models import Cliente, Order

# Crear pizzas de ejemplo
pizzas_data = [
    {
        'nombre': 'Margarita',
        'tipo_masa': 'Masa delgada',
        'ingredientes': 'Tomate, queso mozzarella, albahaca',
        'disponible': True,
    },
    {
        'nombre': 'Pepperoni',
        'tipo_masa': 'Masa tradicional',
        'ingredientes': 'Tomate, queso mozzarella, pepperoni',
        'disponible': True,
    },
    {
        'nombre': 'Vegetariana',
        'tipo_masa': 'Masa integral',
        'ingredientes': 'Tomate, mozzarella, champiñones, pimientos, cebolla',
        'disponible': True,
    },
    {
        'nombre': 'Cuatro Quesos',
        'tipo_masa': 'Masa tradicional',
        'ingredientes': 'Mozzarella, parmesano, gorgonzola, provolone',
        'disponible': True,
    },
    {
        'nombre': 'Hawayana',
        'tipo_masa': 'Masa delgada',
        'ingredientes': 'Tomate, queso mozzarella, jamón, piña',
        'disponible': False,
    },
]

print("Creando pizzas...")
for pizza_data in pizzas_data:
    Pizza.objects.create(**pizza_data)
    print(f"  ✓ Pizza '{pizza_data['nombre']}' creada.")

# Crear clientes de ejemplo
clientes_data = [
    {'nombre': 'Ana López', 'telefono': '555-0101', 'direccion': 'Av. Principal 123'},
    {'nombre': 'Bruno García', 'telefono': '555-0102', 'direccion': 'Calle Los Olivos 456'},
    {'nombre': 'Carla Silva', 'telefono': '555-0103', 'direccion': 'Jr. Las Flores 789'},
    {'nombre': 'Diego Pardo', 'telefono': '555-0104', 'direccion': 'Av. Central 321'},
]

print("\nCreando clientes...")
for cliente_data in clientes_data:
    Cliente.objects.create(**cliente_data)
    print(f"  ✓ Cliente '{cliente_data['nombre']}' creado.")

# Crear órdenes de ejemplo
pizzas = Pizza.objects.all()
clientes = Cliente.objects.all()

órdenes_data = [
    {'cliente': clientes[0], 'pizza': pizzas[0], 'cantidad': 1, 'estado': 'Pendiente'},
    {'cliente': clientes[1], 'pizza': pizzas[1], 'cantidad': 2, 'estado': 'En preparación'},
    {'cliente': clientes[2], 'pizza': pizzas[2], 'cantidad': 1, 'estado': 'Entregado'},
    {'cliente': clientes[3], 'pizza': pizzas[3], 'cantidad': 3, 'estado': 'Pendiente'},
]

print("\nCreando órdenes...")
for orden_data in órdenes_data:
    Order.objects.create(**orden_data)
    print(f"  ✓ Orden creada para {orden_data['cliente'].nombre}.")

print("\n✅ ¡Datos de ejemplo creados exitosamente!")
