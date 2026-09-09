from django.shortcuts import redirect, render
from .forms import PizzaForm
from .models import Pizza


def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas})


def pizza_create(request):
    form = PizzaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pizza_list')

    return render(request, 'pizza/pizza_create.html', {'form': form})
