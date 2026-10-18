from django import forms
from django.test import TestCase

from pizzeria.forms import (
    BootstrapFormMixin,
    CategoriaForm,
    ClienteForm,
    DetallePedidoForm,
    IngredienteForm,
    MetodoPagoForm,
    PedidoForm,
    PizzaForm,
    RecetaPizzaForm,
    RepartidorForm,
)
from pizzeria.models import (
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


class PizzeriaFlowTests(TestCase):
    def test_model_relationships_and_str(self):
        categoria = Categoria.objects.create(nombre='Clásica', descripcion='Sabor tradicional')
        cliente = Cliente.objects.create(nombre='Ana', telefono='999999999')
        DatosEntrega.objects.create(
            cliente=cliente,
            direccion='Av. Siempre Viva 123',
            referencia='Frente al kiosko',
            instrucciones='Tocar timbre 2',
        )
        ingrediente = Ingrediente.objects.create(nombre='Queso', unidad_medida='gr', stock=500)
        metodo_pago = MetodoPago.objects.create(nombre='Tarjeta', descripcion='Visa o Mastercard')
        repartidor = Repartidor.objects.create(nombre='Luis', telefono='111222333', vehiculo='Moto')
        pizza = Pizza.objects.create(
            categoria=categoria,
            nombre='Margarita',
            tipo_masa='fina',
            precio_base=18.50,
            disponible=True,
        )
        RecetaPizza.objects.create(
            pizza=pizza,
            ingrediente=ingrediente,
            cantidad_gramos=200,
            es_opcional=False,
        )
        pedido = Pedido.objects.create(
            cliente=cliente,
            metodo_pago=metodo_pago,
            repartidor=repartidor,
            estado='pendiente',
        )
        DetallePedido.objects.create(
            pedido=pedido,
            pizza=pizza,
            cantidad=2,
            precio_unitario=18.50,
        )

        self.assertEqual(str(categoria), 'Clásica')
        self.assertEqual(str(cliente), 'Ana')
        self.assertEqual(str(ingrediente), 'Queso')
        self.assertEqual(str(metodo_pago), 'Tarjeta')
        self.assertEqual(str(pizza), 'Margarita')
        self.assertEqual(str(repartidor), 'Luis')
        self.assertEqual(str(pedido), f'Pedido #{pedido.pk} - {cliente}')
        self.assertEqual(cliente.datos_entrega.direccion, 'Av. Siempre Viva 123')
        self.assertEqual(pizza.recetas.count(), 1)
        self.assertEqual(pedido.detalles.count(), 1)

    def test_forms_have_bootstrap_classes(self):
        form = PizzaForm()
        self.assertIn('form-select', form.fields['categoria'].widget.attrs.get('class', ''))
        self.assertIn('form-control', form.fields['nombre'].widget.attrs.get('class', ''))

        checkbox_form = CategoriaForm()
        self.assertTrue(hasattr(BootstrapFormMixin, '__init__'))
        self.assertIsInstance(checkbox_form.fields['descripcion'].widget, forms.Textarea)

        pedido_form = PedidoForm()
        self.assertIn('form-select', pedido_form.fields['cliente'].widget.attrs.get('class', ''))

        self.assertIsNotNone(CategoriaForm())
        self.assertIsNotNone(ClienteForm())
        self.assertIsNotNone(IngredienteForm())
        self.assertIsNotNone(RecetaPizzaForm())
        self.assertIsNotNone(MetodoPagoForm())
        self.assertIsNotNone(RepartidorForm())
        self.assertIsNotNone(PedidoForm())
        self.assertIsNotNone(DetallePedidoForm())
