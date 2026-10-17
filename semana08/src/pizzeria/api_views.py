from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Categoria, Cliente, Ingrediente, Pedido, Pizza, Repartidor
from .serializers import (
    CategoriaSerializer,
    ClienteDetailSerializer,
    IngredienteSerializer,
    PedidoReadSerializer,
    PizzaSerializer,
    RepartidorSerializer,
)


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'tipo_masa']
    ordering_fields = ['precio_base', 'nombre']


class PedidoReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PedidoReadSerializer

    def get_queryset(self):
        queryset = Pedido.objects.con_detalle()
        estado = self.request.query_params.get('estado')
        if estado is not None:
            queryset = queryset.filter(estado=estado)
        return queryset

    @action(detail=False, methods=['get'])
    def del_mes(self, request):
        pedidos_mes = Pedido.objects.del_mes().con_detalle()
        serializer = self.get_serializer(pedidos_mes, many=True)
        return Response(serializer.data)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['stock', 'nombre']

    def get_queryset(self):
        queryset = super().get_queryset()
        unidad = self.request.query_params.get('unidad')
        if unidad:
            queryset = queryset.filter(unidad_medida=unidad)
        return queryset

    @action(detail=False, methods=['get'])
    def con_stock(self, request):
        ingredientes_disponibles = Ingrediente.objects.filter(stock__gt=0)
        serializer = self.get_serializer(ingredientes_disponibles, many=True)
        return Response(serializer.data)


class RepartidorViewSet(viewsets.ModelViewSet):
    queryset = Repartidor.objects.all()
    serializer_class = RepartidorSerializer


class ClienteReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClienteDetailSerializer

    def get_queryset(self):
        return Cliente.objects.select_related('datos_entrega').all()
