from decimal import Decimal

from rest_framework.test import APITestCase

from pizzeria.models import (
    Categoria,
    Cliente,
    DatosEntrega,
    DetallePedido,
    Ingrediente,
    MetodoPago,
    Pedido,
    Pizza,
)


class PizzeriaAPITests(APITestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Clásica')
        self.pizza = Pizza.objects.create(
            categoria=self.categoria,
            nombre='Margarita',
            tipo_masa='fina',
            precio_base='18.50',
        )
        self.cliente = Cliente.objects.create(nombre='Ana', telefono='999999999')
        DatosEntrega.objects.create(
            cliente=self.cliente,
            direccion='Av. Siempre Viva 123',
        )
        self.metodo_pago = MetodoPago.objects.create(nombre='Tarjeta')
        self.pedido = Pedido.objects.create(
            cliente=self.cliente,
            metodo_pago=self.metodo_pago,
        )
        DetallePedido.objects.create(
            pedido=self.pedido,
            pizza=self.pizza,
            cantidad=2,
            precio_unitario=Decimal('18.50'),
        )

    def test_pizza_api_supports_crud_and_price_validation(self):
        response = self.client.get('/api/pizzas/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['nombre'], 'Margarita')

        invalid_response = self.client.post(
            '/api/pizzas/',
            {
                'nombre': 'Inválida',
                'categoria': self.categoria.pk,
                'tipo_masa': 'fina',
                'precio_base': '-5.00',
                'disponible': True,
            },
        )
        self.assertEqual(invalid_response.status_code, 400)
        self.assertIn('precio_base', invalid_response.data)

        create_response = self.client.post(
            '/api/pizzas/',
            {
                'nombre': 'Pepperoni',
                'categoria': self.categoria.pk,
                'tipo_masa': 'gruesa',
                'precio_base': '28.00',
                'disponible': True,
            },
        )
        self.assertEqual(create_response.status_code, 201)

        update_response = self.client.patch(
            f'/api/pizzas/{self.pizza.pk}/',
            {'precio_base': '20.00'},
        )
        self.assertEqual(update_response.status_code, 200)
        self.pizza.refresh_from_db()
        self.assertEqual(str(self.pizza.precio_base), '20.00')

        delete_response = self.client.delete(f'/api/pizzas/{create_response.data["id"]}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_pedido_consultation_includes_nested_details_and_month_action(self):
        response = self.client.get('/api/pedidos-consulta/?estado=pendiente')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['cliente_nombre'], 'Ana')
        self.assertEqual(response.data[0]['detalles'][0]['pizza_nombre'], 'Margarita')

        month_response = self.client.get('/api/pedidos-consulta/del_mes/')
        self.assertEqual(month_response.status_code, 200)
        self.assertEqual(len(month_response.data), 1)

    def test_ingredient_search_filters_and_stock_action(self):
        queso = Ingrediente.objects.create(
            nombre='Queso',
            unidad_medida='gr',
            stock=500,
        )
        Ingrediente.objects.create(
            nombre='Harina',
            unidad_medida='kg',
            stock=0,
        )

        response = self.client.get('/api/ingredientes/?search=Queso&unidad=gr&ordering=-stock')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([item['id'] for item in response.data], [queso.pk])

        stock_response = self.client.get('/api/ingredientes/con_stock/')
        self.assertEqual(stock_response.status_code, 200)
        self.assertEqual([item['id'] for item in stock_response.data], [queso.pk])

        invalid_response = self.client.post(
            '/api/ingredientes/',
            {'nombre': 'Negativo', 'unidad_medida': 'gr', 'stock': -50},
        )
        self.assertEqual(invalid_response.status_code, 400)

    def test_related_resource_endpoints_are_available(self):
        category_response = self.client.get('/api/categorias/')
        self.assertEqual(category_response.status_code, 200)

        client_response = self.client.get('/api/clientes-consulta/')
        self.assertEqual(client_response.status_code, 200)
        self.assertEqual(
            client_response.data[0]['datos_entrega']['direccion'],
            'Av. Siempre Viva 123',
        )
