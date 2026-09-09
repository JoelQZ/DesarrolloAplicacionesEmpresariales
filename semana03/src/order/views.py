from django.shortcuts import redirect, render
from .forms import OrderForm, ClienteForm
from .models import Order, Cliente


def order_list(request):
    orders = Order.objects.select_related('cliente', 'pizza').all()
    return render(request, 'order/order_list.html', {'orders': orders})


def order_create(request):
    if request.method == 'POST':
        # Si ya existe el cliente, usarlo; si no, crearlo
        cliente_id = request.POST.get('cliente_id')
        if cliente_id:
            cliente = Cliente.objects.get(id=cliente_id)
        else:
            cliente_form = ClienteForm(request.POST)
            if cliente_form.is_valid():
                cliente = cliente_form.save()
            else:
                return render(request, 'order/order_create.html', {
                    'order_form': OrderForm(),
                    'cliente_form': cliente_form
                })
        
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.cliente = cliente
            order.save()
            return redirect('order_list')
    else:
        order_form = OrderForm()
        cliente_form = ClienteForm()

    return render(request, 'order/order_create.html', {
        'order_form': order_form,
        'cliente_form': cliente_form
    })
