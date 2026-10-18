from rest_framework import serializers

from .models import (
    Categoria,
    Cliente,
    DatosEntrega,
    DetallePedido,
    Ingrediente,
    MetodoPago,
    Pedido,
    Pizza,
    Repartidor,
)


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'nombre', 'categoria', 'tipo_masa', 'precio_base', 'disponible']

    def validate_precio_base(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'El precio base de la pizza debe ser mayor a 0.'
            )
        return value


class DetallePedidoReadSerializer(serializers.ModelSerializer):
    pizza_nombre = serializers.ReadOnlyField(source='pizza.nombre')

    class Meta:
        model = DetallePedido
        fields = [
            'id',
            'pizza',
            'pizza_nombre',
            'cantidad',
            'precio_unitario',
            'subtotal',
        ]


class PedidoReadSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoReadSerializer(many=True, read_only=True)
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')
    metodo_pago_nombre = serializers.ReadOnlyField(source='metodo_pago.nombre')

    class Meta:
        model = Pedido
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'metodo_pago',
            'metodo_pago_nombre',
            'tipo_pedido',
            'fecha_pedido',
            'estado',
            'detalles',
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'unidad_medida', 'stock']

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'El stock no puede ser un valor negativo.'
            )
        return value


class RepartidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repartidor
        fields = '__all__'


class DatosEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosEntrega
        fields = ['direccion', 'referencia', 'instrucciones']


class ClienteDetailSerializer(serializers.ModelSerializer):
    datos_entrega = DatosEntregaSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'telefono', 'datos_entrega']
