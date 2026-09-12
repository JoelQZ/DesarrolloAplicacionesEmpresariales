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