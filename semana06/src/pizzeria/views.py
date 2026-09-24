from django.contrib import messages
from django.db import transaction
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CategoriaForm,
    ClienteForm,
    DatosEntregaForm,
    DetallePedidoForm,
    IngredienteForm,
    MetodoPagoForm,
    PedidoForm,
    PizzaForm,
    RecetaPizzaForm,
    RepartidorForm,
)
from .models import (
    Categoria,
    Cliente,
    DatosEntrega,
    DetallePedido,
    Ingrediente,
    MetodoPago,
    Pedido,
    Pizza,
    RecetaPizza,
    Repartidor,
)


def categoria_list(request):
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'pizzeria/categoria_list.html', {'object_list': categorias})


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'pizzeria/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'pizzeria/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        pizzas_asociadas = Pizza.objects.filter(categoria=categoria)

        if pizzas_asociadas.exists():
            nombres = ", ".join(set(p.nombre for p in pizzas_asociadas))
            messages.error(
                request,
                f'No puedes eliminar la categoría "{categoria.nombre}" porque está asociada a la(s) pizza(s): {nombres}.'
            )
            return redirect('categoria_list')

        try:
            categoria.delete()
            messages.success(request, 'Categoría eliminada correctamente.')
        except ProtectedError:
            messages.error(
                request,
                f'No puedes eliminar la categoría "{categoria.nombre}" porque tiene registros asociados.'
            )
        return redirect('categoria_list')

    return render(
        request,
        'pizzeria/delete_confirm.html',
        {
            'object': categoria,
            'entity': 'Categoría',
            'cancel_url': 'categoria_list',
        },
    )

def cliente_list(request):
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'pizzeria/cliente_list.html', {'object_list': clientes})


def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'pizzeria/cliente_form.html', {'form': form})


def datosentrega_create(request):
    if request.method == 'POST':
        form = DatosEntregaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = DatosEntregaForm()
    return render(request, 'pizzeria/datosentrega_form.html', {'form': form})


def repartidor_list(request):
    repartidores = Repartidor.objects.all().order_by('nombre')
    return render(request, 'pizzeria/repartidor_list.html', {'object_list': repartidores})


def repartidor_create(request):
    if request.method == 'POST':
        form = RepartidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repartidor_list')
    else:
        form = RepartidorForm()
    return render(request, 'pizzeria/repartidor_form.html', {'form': form})

def repartidor_update(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        form = RepartidorForm(request.POST, instance=repartidor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Repartidor actualizado correctamente.')
            return redirect('repartidor_list')
    else:
        form = RepartidorForm(instance=repartidor)
    return render(request, 'pizzeria/repartidor_form.html', {'form': form})


def repartidor_delete(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        pedidos_asociados = Pedido.objects.filter(repartidor=repartidor)

        if pedidos_asociados.exists():
            messages.error(
                request,
                f'No puedes eliminar al repartidor "{repartidor.nombre}" porque tiene {pedidos_asociados.count()} pedido(s) asignado(s).'
            )
            return redirect('repartidor_list')

        try:
            repartidor.delete()
            messages.success(request, 'Repartidor eliminado correctamente.')
        except ProtectedError:
            messages.error(
                request,
                f'No puedes eliminar al repartidor "{repartidor.nombre}" porque tiene registros asociados.'
            )
        return redirect('repartidor_list')

    return render(
        request,
        'pizzeria/delete_confirm.html',
        {
            'object': repartidor,
            'entity': 'Repartidor',
            'cancel_url': 'repartidor_list',
        },
    )

def metodopago_list(request):
    metodos = MetodoPago.objects.all().order_by('nombre')
    return render(request, 'pizzeria/metodopago_list.html', {'object_list': metodos})


def metodopago_create(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('metodopago_list')
    else:
        form = MetodoPagoForm()
    return render(request, 'pizzeria/metodopago_form.html', {'form': form})

def metodopago_update(request, pk):
    metodo = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Método de pago actualizado correctamente.')
            return redirect('metodopago_list')
    else:
        form = MetodoPagoForm(instance=metodo)
    return render(request, 'pizzeria/metodopago_form.html', {'form': form})


def metodopago_delete(request, pk):
    metodo = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        pedidos_asociados = Pedido.objects.filter(metodo_pago=metodo)

        if pedidos_asociados.exists():
            messages.error(
                request,
                f'No puedes eliminar el método de pago "{metodo.nombre}" porque está registrado en {pedidos_asociados.count()} pedido(s).'
            )
            return redirect('metodopago_list')

        try:
            metodo.delete()
            messages.success(request, 'Método de pago eliminado correctamente.')
        except ProtectedError:
            messages.error(
                request,
                f'No puedes eliminar el método de pago "{metodo.nombre}" porque está en uso.'
            )
        return redirect('metodopago_list')

    return render(
        request,
        'pizzeria/delete_confirm.html',
        {
            'object': metodo,
            'entity': 'Método de Pago',
            'cancel_url': 'metodopago_list',
        },
    )

def ingrediente_list(request):
    ingredientes = Ingrediente.objects.all().order_by('nombre')
    return render(request, 'pizzeria/ingrediente_list.html', {'object_list': ingredientes})


def ingrediente_create(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingrediente_list')
    else:
        form = IngredienteForm()
    return render(request, 'pizzeria/ingrediente_form.html', {'form': form})

def ingrediente_update(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('ingrediente_list')
    else:
        form = IngredienteForm(instance=ingrediente)
    return render(request, 'pizzeria/ingrediente_form.html', {'form': form})


def ingrediente_delete(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        recetas = RecetaPizza.objects.filter(ingrediente=ingrediente).select_related('pizza')

        if recetas.exists():
            nombres_pizzas = ", ".join(set(r.pizza.nombre for r in recetas if r.pizza))
            messages.error(
                request,
                f'No puedes eliminar el ingrediente "{ingrediente.nombre}" porque está asociado a la(s) pizza(s): {nombres_pizzas}.'
            )
            return redirect('ingrediente_list')

        ingrediente.delete()
        messages.success(request, 'Ingrediente eliminado correctamente.')
        return redirect('ingrediente_list')

    return render(
        request,
        'pizzeria/delete_confirm.html',
        {
            'object': ingrediente,
            'entity': 'Ingrediente',
            'cancel_url': 'ingrediente_list',
        },
    )

def pizza_list(request):
    pizzas = Pizza.objects.select_related('categoria').all().order_by('nombre')
    return render(request, 'pizzeria/pizza_list.html', {'object_list': pizzas})


def pizza_create(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    else:
        form = PizzaForm()
    return render(request, 'pizzeria/pizza_form.html', {'form': form})

def pizza_update(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizzeria/pizza_form.html', {'form': form})


def pizza_delete(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizza_list')
    return render(request, 'pizzeria/delete_confirm.html', {
        'object': pizza,
        'entity': 'Pizza',
        'cancel_url': 'pizza_list',
    })

def receta_create(request):
    if request.method == 'POST':
        form = RecetaPizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_list')
    else:
        form = RecetaPizzaForm()
    return render(request, 'pizzeria/recetapizza_form.html', {'form': form})


def order_list(request):
    pedidos = (
        Pedido.objects.select_related(
            'cliente',
            'cliente__datos_entrega',
            'metodo_pago',
            'repartidor',
        )
        .prefetch_related('detalles__pizza')
        .all()
        .order_by('-fecha_pedido')
    )
    return render(request, 'pizzeria/order_list.html', {'object_list': pedidos})


def order_create(request):
    pizzas = Pizza.objects.filter(disponible=True).select_related('categoria').order_by('nombre')
    metodos_pago = MetodoPago.objects.all().order_by('nombre')
    repartidores = Repartidor.objects.all().order_by('nombre')

    if request.method == 'POST':
        tipo_pedido = request.POST.get('tipo_pedido', 'presencial')
        nombre_cliente = (request.POST.get('nombre_cliente') or '').strip()
        telefono = (request.POST.get('telefono') or '').strip()
        direccion = (request.POST.get('direccion_entrega') or '').strip()
        metodo_pago_id = request.POST.get('metodo_pago')
        repartidor_id = request.POST.get('repartidor')
        pizza_ids = request.POST.getlist('pizza')

        if not nombre_cliente:
            return render(request, 'pizzeria/order_form.html', {
                'error': 'Debe ingresar el nombre del cliente.',
                'pizzas': pizzas,
                'metodos_pago': metodos_pago,
                'repartidores': repartidores,
            })

        if tipo_pedido == 'delivery':
            if not telefono:
                return render(request, 'pizzeria/order_form.html', {
                    'error': 'Debe ingresar el teléfono del cliente para delivery.',
                    'pizzas': pizzas,
                    'metodos_pago': metodos_pago,
                    'repartidores': repartidores,
                })
            if not direccion:
                return render(request, 'pizzeria/order_form.html', {
                    'error': 'Debe ingresar la dirección de entrega.',
                    'pizzas': pizzas,
                    'metodos_pago': metodos_pago,
                    'repartidores': repartidores,
                })

        if not metodo_pago_id:
            return render(request, 'pizzeria/order_form.html', {
                'error': 'Debe seleccionar un método de pago.',
                'pizzas': pizzas,
                'metodos_pago': metodos_pago,
                'repartidores': repartidores,
            })

        if not pizza_ids:
            return render(request, 'pizzeria/order_form.html', {
                'error': 'Debe seleccionar al menos una pizza.',
                'pizzas': pizzas,
                'metodos_pago': metodos_pago,
                'repartidores': repartidores,
            })

        cliente = Cliente.objects.filter(nombre__iexact=nombre_cliente).first()
        if cliente is None:
            cliente = Cliente.objects.create(nombre=nombre_cliente, telefono=telefono or '')

        if tipo_pedido == 'delivery':
            if telefono and cliente.telefono != telefono:
                cliente.telefono = telefono
                cliente.save()
            if direccion:
                datos_entrega, _ = DatosEntrega.objects.get_or_create(
                    cliente=cliente,
                    defaults={'direccion': direccion},
                )
                if datos_entrega.direccion != direccion:
                    datos_entrega.direccion = direccion
                    datos_entrega.save()

        repartidor = None
        if tipo_pedido == 'delivery' and repartidor_id:
            repartidor = get_object_or_404(Repartidor, pk=repartidor_id)

        with transaction.atomic():
            pedido = Pedido.objects.create(
                cliente=cliente,
                metodo_pago_id=metodo_pago_id,
                repartidor=repartidor,
                tipo_pedido=tipo_pedido,
                estado='pendiente',
            )

            for pizza_id in pizza_ids:
                cantidad = int(request.POST.get(f'cantidad_{pizza_id}', 1) or 1)
                if cantidad <= 0:
                    continue
                pizza = get_object_or_404(Pizza, pk=pizza_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    pizza=pizza,
                    cantidad=cantidad,
                    precio_unitario=pizza.precio_base,
                )

        return redirect('order_list')

    return render(request, 'pizzeria/order_form.html', {
        'pizzas': pizzas,
        'metodos_pago': metodos_pago,
        'repartidores': repartidores,
    })


def detallepedido_create(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.pedido = pedido
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario
            detalle.save()
            return redirect('order_list')
    else:
        form = DetallePedidoForm(initial={'pedido': pedido})
    return render(request, 'pizzeria/detallepedido_form.html', {'form': form, 'pedido': pedido})


def detallepedido_update(request, pk):
    detalle = get_object_or_404(DetallePedido, pk=pk)
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST, instance=detalle)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario
            detalle.save()
            return redirect('order_list')
    else:
        form = DetallePedidoForm(instance=detalle)
    return render(request, 'pizzeria/detallepedido_form.html', {'form': form, 'pedido': detalle.pedido})


def detallepedido_delete(request, pk):
    detalle = get_object_or_404(DetallePedido, pk=pk)
    if request.method == 'POST':
        pedido = detalle.pedido
        detalle.delete()
        return redirect('order_list')
    return render(request, 'pizzeria/delete_confirm.html', {
        'object': detalle,
        'entity': 'detalle del pedido',
        'cancel_url': 'order_list',
    })
