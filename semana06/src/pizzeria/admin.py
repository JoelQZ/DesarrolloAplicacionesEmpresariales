from django.contrib import admin

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


class DatosEntregaInline(admin.StackedInline):
	model = DatosEntrega
	extra = 0


class RecetaPizzaInline(admin.TabularInline):
	model = RecetaPizza
	extra = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'telefono')
	search_fields = ('nombre', 'telefono')
	inlines = [DatosEntregaInline]


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'tipo_masa', 'precio_base', 'disponible')
	search_fields = ('nombre', 'categoria__nombre')
	list_filter = ('categoria', 'disponible')
	inlines = [RecetaPizzaInline]


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'unidad_medida', 'stock')
	search_fields = ('nombre',)
	list_filter = ('unidad_medida',)


admin.site.register([
	Categoria,
	DatosEntrega,
	DetallePedido,
	MetodoPago,
	Pedido,
	RecetaPizza,
	Repartidor,
])
