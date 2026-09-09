from django.shortcuts import get_object_or_404, redirect, render

from .models import Cancha, Cliente, Horario, Reserva, Sede


def inicio(request):
    return render(request, 'canchas/inicio.html')


def reserva_create(request):
    if request.method == 'POST':
        Reserva.objects.create(
            cliente_id=request.POST['cliente'],
            horario_id=request.POST['horario'],
            pagado='pagado' in request.POST,
        )
        return redirect('reserva_list')

    clientes = Cliente.objects.all()
    horarios = Horario.objects.filter(disponible=True)
    return render(request, 'canchas/reserva_form.html', {
        'clientes': clientes,
        'horarios': horarios,
    })

def cliente_create(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            email=request.POST.get('email', ''),
        )
        return redirect('cliente_list')
    return render(request, 'canchas/cliente_form.html')


def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST.get('email', '')
        cliente.save()
        return redirect('cliente_list')
    return render(request, 'canchas/cliente_form.html', {'cliente': cliente})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'canchas/delete_confirm.html', {
        'object': cliente,
        'entity': 'cliente',
        'cancel_url': 'cliente_list',
    })


def sede_create(request):
    if request.method == 'POST':
        Sede.objects.create(
            nombre=request.POST['nombre'],
            direccion=request.POST['direccion'],
        )
        return redirect('sede_list')
    return render(request, 'canchas/sede_form.html')


def sede_update(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == 'POST':
        sede.nombre = request.POST['nombre']
        sede.direccion = request.POST['direccion']
        sede.save()
        return redirect('sede_list')
    return render(request, 'canchas/sede_form.html', {'sede': sede})


def sede_delete(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == 'POST':
        sede.delete()
        return redirect('sede_list')
    return render(request, 'canchas/delete_confirm.html', {
        'object': sede,
        'entity': 'sede',
        'cancel_url': 'sede_list',
    })


def cancha_create(request):
    if request.method == 'POST':
        Cancha.objects.create(
            nombre=request.POST['nombre'],
            tipo=request.POST['tipo'],
            precio_hora=request.POST['precio_hora'],
        )
        return redirect('cancha_list')
    return render(request, 'canchas/cancha_form.html')


def cancha_update(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == 'POST':
        cancha.nombre = request.POST['nombre']
        cancha.tipo = request.POST['tipo']
        cancha.precio_hora = request.POST['precio_hora']
        cancha.save()
        return redirect('cancha_list')
    return render(request, 'canchas/cancha_form.html', {'cancha': cancha})


def cancha_delete(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == 'POST':
        cancha.delete()
        return redirect('cancha_list')
    return render(request, 'canchas/delete_confirm.html', {
        'object': cancha,
        'entity': 'cancha',
        'cancel_url': 'cancha_list',
    })


def horario_create(request):
    if request.method == 'POST':
        Horario.objects.create(
            cancha_id=request.POST['cancha'],
            fecha=request.POST['fecha'],
            hora_inicio=request.POST['hora_inicio'],
            hora_fin=request.POST['hora_fin'],
            disponible='disponible' in request.POST,
        )
        return redirect('horario_list')
    canchas = Cancha.objects.all()
    return render(request, 'canchas/horario_form.html', {'canchas': canchas})


def horario_update(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        horario.cancha_id = request.POST['cancha']
        horario.fecha = request.POST['fecha']
        horario.hora_inicio = request.POST['hora_inicio']
        horario.hora_fin = request.POST['hora_fin']
        horario.disponible = 'disponible' in request.POST
        horario.save()
        return redirect('horario_list')
    return render(request, 'canchas/horario_form.html', {
        'horario': horario,
        'canchas': Cancha.objects.all().order_by('nombre'),
    })


def horario_delete(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        horario.delete()
        return redirect('horario_list')
    return render(request, 'canchas/delete_confirm.html', {
        'object': horario,
        'entity': 'horario',
        'cancel_url': 'horario_list',
    })



def cliente_list(request):
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'canchas/cliente_list.html', {'clientes': clientes})

def sede_list(request):
    sedes = Sede.objects.all().order_by('nombre')
    return render(request, 'canchas/sede_list.html', {'sedes': sedes})

def cancha_list(request):
    canchas = Cancha.objects.all().order_by('tipo')
    return render(request, 'canchas/cancha_list.html', {'canchas': canchas})

def horario_list(request):
    horarios = Horario.objects.all().order_by('fecha', 'hora_inicio')
    return render(request, 'canchas/horario_list.html', {'horarios': horarios})

def reserva_list(request):
    reservas = Reserva.objects.all().order_by('-fecha_reserva')
    return render(request, 'canchas/reserva_list.html', {'reservas': reservas})

def reserva_update(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.cliente_id = request.POST['cliente']
        reserva.horario_id = request.POST['horario']
        reserva.pagado = 'pagado' in request.POST
        reserva.save()
        return redirect('reserva_list')

    clientes = Cliente.objects.all()
    horarios = Horario.objects.all()
    return render(request, 'canchas/reserva_form.html', {
        'reserva': reserva,
        'clientes': clientes,
        'horarios': horarios,
    })


def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_list')
    return render(request, 'canchas/delete_confirm.html', {
        'object': reserva,
        'entity': 'reserva',
        'cancel_url': 'reserva_list',
    })