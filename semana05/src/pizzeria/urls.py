from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/nueva/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/datos-entrega/', views.datosentrega_create, name='datosentrega_create'),

    path('repartidores/', views.repartidor_list, name='repartidor_list'),
    path('repartidores/nuevo/', views.repartidor_create, name='repartidor_create'),
    path('repartidores/<int:pk>/editar/', views.repartidor_update, name='repartidor_update'),
    path('repartidores/<int:pk>/eliminar/', views.repartidor_delete, name='repartidor_delete'),

    path('metodos-pago/', views.metodopago_list, name='metodopago_list'),
    path('metodos-pago/nuevo/', views.metodopago_create, name='metodopago_create'),
    path('metodos-pago/<int:pk>/editar/', views.metodopago_update, name='metodopago_update'),
    path('metodos-pago/<int:pk>/eliminar/', views.metodopago_delete, name='metodopago_delete'),

    path('ingredientes/', views.ingrediente_list, name='ingrediente_list'),
    path('ingredientes/nuevo/', views.ingrediente_create, name='ingrediente_create'),
    path('ingredientes/<int:pk>/editar/', views.ingrediente_update, name='ingrediente_update'),
    path('ingredientes/<int:pk>/eliminar/', views.ingrediente_delete, name='ingrediente_delete'),
    
    path('pizzas/', views.pizza_list, name='pizza_list'),
    path('pizzas/nueva/', views.pizza_create, name='pizza_create'),
    path('pizzas/<int:pk>/editar/', views.pizza_update, name='pizza_update'),
    path('pizzas/<int:pk>/eliminar/', views.pizza_delete, name='pizza_delete'),
    
    path('recetas/nueva/', views.receta_create, name='receta_create'),
    path('pedidos/', views.order_list, name='order_list'),
    path('pedidos/nuevo/', views.order_create, name='order_create'),
    path('pedidos/<int:pedido_id>/detalle/nuevo/', views.detallepedido_create, name='detallepedido_create'),
    path('detalles/<int:pk>/editar/', views.detallepedido_update, name='detallepedido_update'),
    path('detalles/<int:pk>/eliminar/', views.detallepedido_delete, name='detallepedido_delete'),
]