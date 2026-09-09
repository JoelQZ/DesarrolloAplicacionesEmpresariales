from django.shortcuts import redirect, render

from .forms import PizzaForm
from .models import PIZZAS_DB


def pizza_list(request):
    return render(request, 'pizza/pizza_list.html', {'pizzas': PIZZAS_DB})


def pizza_create(request):
    form = PizzaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        PIZZAS_DB.append(form.cleaned_data)
        return redirect('pizza_list')

    return render(request, 'pizza/pizza_create.html', {'form': form})