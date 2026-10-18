# django_project

Aplicacion academica sencilla construida con Django 5. El codigo fuente esta separado en `src/`, con el proyecto `config` y la aplicacion `core`.

## Instalacion en Windows

Desde la raiz del proyecto:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activacion, puede usarse CMD:

```cmd
venv\Scripts\activate
```

## Migraciones y ejecucion

```powershell
cd src
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

La aplicacion queda disponible en <http://127.0.0.1:8000/> y el administrador en <http://127.0.0.1:8000/admin/>.

## Crear un superusuario

Con la terminal ubicada en `src/` y el entorno virtual activo:

```powershell
python manage.py createsuperuser
```

Sigue las indicaciones para definir usuario, correo y contrasena.

## Pruebas

```powershell
python manage.py test
```

## GitHub

El proyecto esta preparado para Git. `venv/`, `__pycache__/`, `db.sqlite3` y archivos locales estan excluidos mediante `.gitignore`.

```powershell
git init
git branch -M main
git add .
git commit -m "Proyecto inicial Django 5"
```

No se configura ningun remoto ni se realiza `push` automaticamente.

# Sistema de Gestión de Pizzería - Semana 02

Aplicación web académica desarrollada en Django 5 para la gestión de una pizzería, incluyendo el control del menú de pizzas y el registro de pedidos de clientes.

## Problemática y Requisitos Funcionales
El sistema aborda la problemática del control operativo de una pizzería mediante dos módulos principales:
1. **Menú (`pizza`)**: Permite listar las especialidades de la casa y registrar nuevas pizzas (nombre, tipo de masa, ingredientes y estado del stock).
2. **Pedidos (`order`)**: Permite visualizar las órdenes registradas y agregar nuevos pedidos de clientes (nombre, teléfono, pizza solicitada, dirección y estado del pedido).

## Arquitectura y Restricciones del Laboratorio
* **Persistencia en Memoria RAM**: Siguiendo las restricciones del laboratorio, **no se utiliza base de datos relacional (SQL) ni el ORM de Django (`models.Model`)**. La información se gestiona mediante listas de diccionarios en memoria en `models.py` (`PIZZAS_DB` y `ORDERS_DB`). Los datos son volátiles y se reinician junto con el servidor.
* **Formularios**: Implementados mediante la clase `forms.Form` con campos validados (`CharField`, `ChoiceField`, `Textarea`).
* **Heredabilidad de Plantillas**: Vistas basadas en plantillas HTML que extienden de la estructura base unificada `core/base.html`.

## Estructura de Apps
* `pizza`: Aplicación encargada del menú y catálogo de productos.
* `order`: Aplicación encargada del registro y flujo de delivery/pedidos.
* `core`: Aplicación base que provee el diseño estructural del proyecto.

## Instalación y Ejecución

1. Activar el entorno virtual desde la raíz del proyecto:
   ```powershell
   .\venv\Scripts\Activate.ps1

## Configuración e Integración con Django Admin (Semana 05)

Se configuró el panel de administración de Django (`src/pizzeria/admin.py`) para gestionar de forma centralizada la base de datos relacional de la pizzería y los modelos de la investigación.

### Modelos Registrados y Personalizaciones

1. **Gestión de Clientes y Entidades Relacionadas:**
   * **`Cliente` (`ClienteAdmin`):** Configurado con `list_display` (`nombre`, `telefono`) y `search_fields` (`nombre`, `telefono`). Integra la relación $1:1$ mediante **`DatosEntregaInline`** (`admin.StackedInline`), permitiendo gestionar los datos de entrega en la misma vista.
   * **`DatosEntrega`:** Registrado y expuesto de forma apilada en la vista principal de Cliente.

2. **Gestión del Catálogo y Recetas (N:M):**
   * **`Pizza` (`PizzaAdmin`):** Personalizado con `list_display` (`nombre`, `categoria`, `tipo_masa`, `precio_base`, `disponible`) y `list_filter` (`disponible`, `categoria`). Integra la relación $N:M$ mediante **`RecetaPizzaInline`** (`admin.TabularInline`), permitiendo editar los ingredientes y gramos directamente en la pizza.
   * **`Ingrediente` (`IngredienteAdmin`):** Configurado con `list_display` (`nombre`, `unidad_medida`, `stock`), `search_fields` (`nombre`) y `list_filter` (`unidad_medida`).
   * **`RecetaPizza`:** Modelo intermedio que gestiona la relación entre `Pizza` e `Ingrediente`.

3. **Gestión Operativa y Auxiliar:**
   * **`Pedido`, `DetallePedido`, `Categoria`, `MetodoPago`, `Repartidor`:** Registrados mediante `@admin.register` para la gestión CRUD completa del ciclo de ventas.

## 🛠️ Refactorización de Plantillas (Semana 06)

En esta fase del proyecto se optimizó la capa de presentación mediante técnicas avanzadas de plantillas en Django, aplicando el principio **DRY (Don't Repeat Yourself)**, modularización y validación de seguridad.

### 1. Herencia de Plantillas (`{% extends %}`)
Se creó un maquetado base unificado (`base.html`) utilizando **Bootstrap 5**, que incluye la barra lateral (*sidebar*), el encabezado y el pie de página. Se migró la totalidad de las plantillas del sistema para heredar de este diseño base:
* **Entidades refactorizadas:** `Pizza`, `Ingrediente`, `Categoría`, `Cliente`, `Pedido`, `Repartidor`, `Pago`.
* **Archivos clave:** `pizza_list.html`, `categoria_list.html`, `ingrediente_form.html`, entre otros.

### 2. Filtros de Plantillas (*Template Filters*)
Se aplicaron filtros nativos de Django para dar formato a los datos presentados al usuario:
* `floatformat:2`: Para la presentación limpia de los precios y montos monetarios (ej. `S/ 27.00`).
* `upper`: Para estandarizar nombres de categorías y títulos de productos.
* `default`: Para manejar valores nulos o descripciones vacías (ej. *"Sin descripción"*).

### 3. Modularización con Parciales (`{% include %}`)
Se identificaron y extrajeron bloques HTML repetitivos hacia componentes independientes para facilitar su mantenimiento:
* `_header.html`: Encabezados estandarizados para las tarjetas de listado y formularios.
* `_messages.html`: Bloque de alertas y notificaciones del sistema (`django.contrib.messages`).

### 4. Seguridad y Validación XSS
Se comprobó la protección nativa de Django contra ataques **Cross-Site Scripting (XSS)**. El motor de plantillas aplica *auto-escaping* por defecto, transformando caracteres especiales como `<script>` en entidades HTML seguras (`&lt;script&gt;`).

## 🛠️ Arquitectura de API REST con Django REST Framework (Semana 08)

En esta fase del proyecto se diseñó e implementó la API RESTful utilizando **Django REST Framework (DRF)**, aplicando serialización avanzada, ViewSets, enrutamiento automático, validaciones de negocio y optimización de consultas a la base de datos.

### 1. Serialización y Validaciones de Negocio (`serializers.py`)
Se crearon clases basadas en `ModelSerializer` para la transformación bidireccional entre los modelos de la base de datos y formato JSON, incorporando reglas de validación personalizadas:
* **Validación de campos (`validate_<campo>`):** Implementada en `IngredienteSerializer` mediante `validate_stock()` para impedir el registro o actualización de insumos con stock negativo (`stock < 0`).
* **Relaciones anidadas (Nested Serializers):** `ClienteDetailSerializer` expone en una relación $1:1$ los datos del modelo `DatosEntrega`, permitiendo obtener la información completa del cliente en una sola petición.
* **Separación de responsabilidades de lectura/escritura:** Implementación de `PedidoReadSerializer` y `DetallePedidoReadSerializer` para presentar respuestas enriquecidas con los nombres y detalles de las pizzas.

### 2. Controladores y Vistas de API (`api_views.py`)
Se implementaron arquitecturas de vistas basadas en ViewSets para simplificar las operaciones CRUD y de solo lectura:
* **`ModelViewSet`:** Aplicado en `CategoriaViewSet`, `PizzaViewSet`, `IngredienteViewSet` y `RepartidorViewSet` para la gestión CRUD completa.
* **`ReadOnlyModelViewSet`:** Aplicado en `PedidoReadOnlyViewSet` y `ClienteReadOnlyViewSet` para proteger los datos de modificaciones no autorizadas a través de la API.
* **Enrutamiento automático (`DefaultRouter`):** Configurado en `urls.py` bajo el prefijo `/api/`, registrando y exponiendo automáticamente las rutas HTTP (GET, POST, PUT, DELETE) y la interfaz interactiva navegable de DRF.

### 3. Filtros, Ordenamiento y Acciones Personalizadas (`@action`)
Se añadieron capacidades avanzadas de búsqueda y filtrado dinámico sobre los endpoints de la API:
* **Filtros globales de DRF (`SearchFilter`, `OrderingFilter`):**
  * `PizzaViewSet`: Permite búsquedas parciales (`?search=fina`) y ordenamiento por precio (`?ordering=-precio_base`).
  * `IngredienteViewSet`: Habilita búsqueda por nombre y ordenamiento por nivel de stock.
* **Filtros por parámetros de consulta (`Query Params`):**
  * Sobrescritura del método `get_queryset()` en `PedidoReadOnlyViewSet` para filtrar por estado (`?estado=pendiente`).
  * Filtrado por unidad de medida (`?unidad=gr`) en `IngredienteViewSet`.
* **Acciones personalizadas (`@action`):**
  * `@action(detail=False)` en `del_mes/`: Expone en `/api/pedidos-consulta/del_mes/` la consulta reutilizada del `PedidoQuerySet`.
  * `@action(detail=False)` en `con_stock/`: Expone en `/api/ingredientes/con_stock/` el listado de ingredientes con inventario disponible (`stock > 0`).

### 4. Optimización de Consultas SQL (Evitación del Problema N+1)
Se evaluó el rendimiento de la API midiendo la cantidad de consultas enviadas a la base de datos mediante `len(connection.queries)` en la terminal interactiva:
* **Optimización con `select_related`:** Aplicado sobre relaciones de tipo clave foránea y $1:1$ (como `datos_entrega` en `ClienteReadOnlyViewSet`), logrando reducir múltiples ejecuciones de queries a una sola consulta optimizada mediante `JOIN` en SQL.

# Pizzería Gran Sabor — Semana 09: Front-end con React y Vite

En esta fase del proyecto se diseñó e implementó la Single Page Application (SPA) utilizando **React** y **Vite**, migrando la interfaz desde los Templates de Django hacia una arquitectura cliente-servidor renderizada en el navegador, aplicando componentes funcionales, expresiones JSX, iteración de listas con claves únicas, renderizado condicional avanzado y estructuración modular con estilos personalizables.

### 1. Entorno de Desarrollo y Estructura del Proyecto
Se configuró el entorno de ejecución basado en Node.js y npm, utilizando Vite para el andamiaje inicial del cliente React dentro del directorio `frontend/`:
* **Punto de Entrada SPA (`index.html` y `main.jsx`):** Definición del documento HTML único y montaje del componente raíz `App` en el DOM mediante `createRoot`.
* **Organización del Código (`src/`):** Centralización de la lógica del cliente en `App.jsx`, maquetado modular de vistas y aislamiento de reglas de estilos globales y de componentes en `App.css`.
* **Gestión de Dependencias y Scripts (`package.json`):** Definición de librerías base de React, scripts de desarrollo (`npm run dev`), análisis sintáctico (`npm run lint`) y compilación para producción (`npm run build`). Exclusión estricta de las carpetas `node_modules/` y `dist/` a través de `.gitignore`.

### 2. Lógica de Interfaz y Expresiones JSX
Se reemplazó la sintaxis tradicional de plantillas HTML por componentes JSX, permitiendo incrustar lógica de JavaScript directamente en el renderizado mediante llaves `{}`:
* **Inyección de Expresiones e Impuestos:** Definición del precio base familiar y cálculo dinámico en tiempo de ejecución del valor con IGV (18%) aplicando formateo numérico con `.toFixed(2)`.
* **Mapeo de Entidades (`.map()`):** Construcción de vistas iterativas para el catálogo de pizzas utilizando el método `.map()`, garantizando el rastreo del DOM mediante la asignación explícita de claves únicas (`key={pizza.id}`).

### 3. Renderizado Condicional y Relaciones Anidadas
Se incorporaron mecanismos dinámicos para modificar la presentación visual según el estado de los datos:
* **Operadores Ternarios y Evaluación Lógica `&&`:** Implementación de ternarios para alternar clases CSS y mensajes de disponibilidad (`Disponible` vs `Agotado`), combinados con evaluaciones lógicas `&&` para resaltar alertas de agotamiento temporal (`!pizza.disponible && ...`) y validaciones de arreglos vacíos (`pizzas.length === 0`).
* **Listas Anidadas en Relaciones $1:N$:** Visualización del historial de ventas asociando cada pedido con su arreglo interno de ítems mediante un `.map()` principal y un `.map()` anidado, realizando la suma acumulada del total del pedido en tiempo real mediante funciones reductoras de JavaScript.

### 4. Investigación Propia: Control de Inventario, Repartidores y Recetas
Se extendió la interfaz cliente para abarcar los modelos avanzados desarrollados en las fases previas del proyecto:
* **Gestión de Stock de Ingredientes:** Despliegue del listado de insumos con alertas condicionales automáticas (`¡Reabastecer pronto!`) cuando el inventario cae por debajo del nivel mínimo o se encuentra agotado.
* **Control de Repartidores y Composición N:M:** Monitoreo del estado operativo del personal de entrega (`Activo` / `Inactivo`) y maquetado anidado del modelo intermedio de recetas para desglosar la cantidad de insumos requeridos por pizza y calcular el costo total de producción en tiempo real.

---

## 🛠️ Requisitos Previos e Instalación

Para ejecutar este proyecto en su entorno local, asegúrese de contar con **Node.js** (v18.0 o superior) y **npm** instalados.

Siga los pasos a continuación para iniciar la aplicación:

1. **Ingresar al directorio del frontend:**
   ```bash
   cd frontend
   Instalar las dependencias:
   npm install
   Iniciar el servidor de desarrollo:
   npm run dev
   Verificar sintaxis y construir para producción:
   npm run lint
   npm run build

---