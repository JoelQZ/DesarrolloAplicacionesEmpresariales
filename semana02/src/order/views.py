from django.shortcuts import redirect, render

from .forms import OrderForm
from .models import ORDERS_DB


def order_list(request):
    return render(request, 'order/order_list.html', {'orders': ORDERS_DB})


def order_create(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ORDERS_DB.append(form.cleaned_data)
        return redirect('order_list')

    return render(request, 'order/order_create.html', {'form': form})