from django import forms

ESTADO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('En preparación', 'En preparación'),
    ('Entregado', 'Entregado'),
    ('Cancelado', 'Cancelado'),
]


class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100, label='Nombre del Cliente')
    phone = forms.CharField(max_length=30, label='Teléfono')
    pizza_name = forms.CharField(max_length=100, label='Pizza Solicitada')
    address = forms.CharField(widget=forms.Textarea, label='Dirección de Envío')
    status = forms.ChoiceField(
        choices=ESTADO_CHOICES, label='Estado del Pedido', widget=forms.Select
    )