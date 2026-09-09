from django import forms
from .models import Order, Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion']
        labels = {
            'nombre': 'Nombre del Cliente',
            'telefono': 'Teléfono',
            'direccion': 'Dirección de Envío',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 555-0101'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Av. Principal 123',
                'rows': 3
            }),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cliente', 'pizza', 'cantidad', 'estado']
        labels = {
            'cliente': 'Cliente',
            'pizza': 'Pizza Solicitada',
            'cantidad': 'Cantidad',
            'estado': 'Estado del Pedido',
        }
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pizza': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
