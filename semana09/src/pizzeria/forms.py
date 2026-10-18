from django import forms

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


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs['class'] = 'form-check-input'
            elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
                widget.attrs['class'] = 'form-select'
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                pass
            else:
                widget.attrs['class'] = 'form-control'


class CategoriaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class PizzaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple(),
        }


class IngredienteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class RecetaPizzaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RecetaPizza
        fields = '__all__'


class ClienteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class DatosEntregaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = DatosEntrega
        fields = '__all__'


class MetodoPagoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class RepartidorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = '__all__'


class PedidoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class DetallePedidoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'
