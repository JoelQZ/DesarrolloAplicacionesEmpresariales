Ejercicios de Django 5 con Visual Studio Code y GitHub Copilot

Introducción

Este documento contiene una guía paso a paso para desarrollar un proyecto web con Django 5, utilizando Python, Visual Studio Code y GitHub Copilot.

El proyecto se llamará django_project y tendrá una estructura organizada separando el código fuente (src/) de la configuración del proyecto (config/) y de la aplicación principal (core/).

Al finalizar los ejercicios se tendrá:

Un entorno virtual de Python.

Django 5 instalado.

Un proyecto Django llamado config.

Una aplicación llamada core.

Un modelo Item.

Migraciones configuradas y aplicadas.

Vistas y URLs.

Plantillas HTML con herencia.

Panel de administración de Django.

Datos de prueba.

Un archivo requirements.txt.

Un archivo README.md.

Un repositorio publicado en GitHub.

1. Preparar el entorno de trabajo

1.1. Crear la carpeta del proyecto

Abrir una terminal en Visual Studio Code y ejecutar:

mkdir django_project
cd django_project

También se puede abrir directamente la carpeta desde Visual Studio Code:

code .

La carpeta principal del proyecto será:

django_project/

1.2. Crear el entorno virtual

Dentro de django_project, ejecutar:

py -m venv venv

Esto crea un entorno virtual llamado venv.

1.3. Activar el entorno virtual

En Windows PowerShell:

.\venv\Scripts\Activate.ps1

Si se utiliza CMD:

venv\Scripts\activate

Cuando el entorno está activo, la terminal debería mostrar algo similar a:

(venv) PS C:\...\django_project>

1.4. Crear la carpeta src

Con el entorno virtual activado:

mkdir src

La estructura inicial será:

django_project/
├── venv/
└── src/

Nota: La carpeta venv contiene el entorno virtual y no debe subirse al repositorio de GitHub.

2. Instalar Django 5

Con venv activado, actualizar pip:

python -m pip install --upgrade pip

Instalar Django 5:

python -m pip install "Django>=5,<6"

Comprobar la instalación:

python -m django --version

Debe aparecer una versión de Django perteneciente a la serie 5.x.

También se puede utilizar:

django-admin --version

Verificación de Python y pip

Es recomendable comprobar que los comandos utilizan el entorno virtual:

python --version
python -m pip --version

3. Crear el proyecto con configuración separada

Entrar en la carpeta src:

cd src

Crear el proyecto utilizando django-admin:

django-admin startproject config .

El punto final (.) es importante porque indica que el proyecto debe crearse en la carpeta actual.

La estructura será:

django_project/
├── venv/
└── src/
    ├── manage.py
    └── config/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

De esta manera:

manage.py queda directamente dentro de src/.

La configuración de Django queda dentro de src/config/.

Probar que el proyecto funciona

Desde src/:

python manage.py check

Si todo está correcto, Django mostrará:

System check identified no issues (0 silenced).

4. Crear y registrar la aplicación core

Desde la carpeta src/:

python manage.py startapp core

La estructura comenzará a ser:

src/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── core/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py

Registrar la aplicación

Abrir:

src/config/settings.py

Buscar INSTALLED_APPS y agregar core:

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

También se puede utilizar:

"core.apps.CoreConfig",

5. Definir el modelo Item

Abrir:

src/core/models.py

Definir el modelo:

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

Explicación de los campos

Campo

Tipo

Descripción

name

CharField

Nombre del ítem

description

TextField

Descripción larga y opcional

created_at

DateTimeField

Fecha y hora de creación automática

blank=True permite que el campo description quede vacío en formularios.

auto_now_add=True registra automáticamente la fecha y hora en que se crea cada objeto.

El método __str__() permite mostrar el nombre del ítem en el panel de administración.

Crear las migraciones

Desde src/:

python manage.py makemigrations

Aplicar las migraciones

python manage.py migrate

Django creará las tablas correspondientes en la base de datos.

6. Crear la vista y las URLs

6.1. Crear la vista

Abrir:

src/core/views.py

Agregar:

from django.shortcuts import render

from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, "core/item_list.html", {"items": items})

La vista:

Obtiene todos los objetos Item.

Los almacena en la variable items.

Envía los datos a la plantilla core/item_list.html.

6.2. Crear las URLs de core

Crear el archivo:

src/core/urls.py

Contenido:

from django.urls import path

from .views import item_list


urlpatterns = [
    path("", item_list, name="item_list"),
]

6.3. Enlazar las URLs de core

Abrir:

src/config/urls.py

Configurar:

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

Con esta configuración:

http://127.0.0.1:8000/

mostrará la vista item_list.

El panel de administración estará disponible en:

http://127.0.0.1:8000/admin/

7. Crear las plantillas

7.1. Crear la estructura de templates

Dentro de src/core/ crear:

templates/
└── core/
    └── item_list.html

Además, se puede crear una plantilla base en:

src/core/templates/base.html

La estructura será:

core/
└── templates/
    ├── base.html
    └── core/
        └── item_list.html

7.2. Crear base.html

Contenido:

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Project{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Mi proyecto Django</h1>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>

7.3. Crear core/item_list.html

Contenido:

{% extends "base.html" %}

{% block title %}Listado de ítems{% endblock %}

{% block content %}
    <h2>Listado de ítems</h2>

    {% for item in items %}
        <article>
            <h3>{{ item.name }}</h3>

            {% if item.description %}
                <p>{{ item.description }}</p>
            {% else %}
                <p>Sin descripción.</p>
            {% endif %}

            <small>Creado: {{ item.created_at }}</small>
        </article>
    {% empty %}
        <p>No existen ítems registrados.</p>
    {% endfor %}
{% endblock %}

Conceptos utilizados

La plantilla utiliza:

{% extends %} para heredar de base.html.

{% block %} para definir contenido.

{% for %} para recorrer los objetos.

{% empty %} para mostrar un mensaje cuando no existen registros.

{{ item.name }} para mostrar información del modelo.

{% if %} para comprobar si existe una descripción.

8. Configurar el administrador y cargar datos

8.1. Registrar Item en el administrador

Abrir:

src/core/admin.py

Agregar:

from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")

Esto permite administrar los objetos Item desde el panel de Django.

8.2. Crear un superusuario

Desde src/:

python manage.py createsuperuser

Django solicitará:

Username:
Email address:
Password:
Password (again):

La contraseña no se mostrará mientras se escribe.

8.3. Iniciar el servidor

python manage.py runserver

Abrir:

http://127.0.0.1:8000/admin/

Iniciar sesión con las credenciales del superusuario.

8.4. Registrar datos de prueba

Desde el panel de administración, seleccionar Items y crear al menos dos registros.

Por ejemplo:

Item 1

Nombre: Laptop
Descripción: Equipo portátil para desarrollo de software.

Item 2

Nombre: Monitor
Descripción: Monitor externo para trabajar con mayor espacio de pantalla.

9. Verificar el funcionamiento

Con el servidor ejecutándose:

python manage.py runserver

Comprobar la página principal:

http://127.0.0.1:8000/

Debe aparecer el listado de los ítems creados desde el administrador.

También comprobar:

http://127.0.0.1:8000/admin/

Debe aparecer el panel de administración de Django.

Lista de comprobación

El servidor inicia correctamente.

La página principal carga sin errores.

Los ítems aparecen en el listado.

El mensaje {% empty %} funciona si no existen registros.

El panel /admin/ funciona.

El superusuario puede iniciar sesión.

Los ítems pueden crearse desde el administrador.

Los ítems pueden editarse y eliminarse.

10. Documentar y subir el proyecto a GitHub

10.1. Generar requirements.txt

Desde la carpeta donde está activo el entorno virtual:

python -m pip freeze > requirements.txt

El archivo contendrá las dependencias instaladas, incluyendo Django.

10.2. Crear .gitignore

En la raíz django_project/, crear:

.gitignore

Contenido recomendado:

venv/
__pycache__/
*.py[cod]
db.sqlite3
.env
.vscode/

Esto evita subir archivos innecesarios o información local al repositorio.

10.3. Estructura final recomendada

django_project/
├── .gitignore
├── README.md
├── requirements.txt
├── venv/
└── src/
    ├── manage.py
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── core/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── __init__.py
        ├── models.py
        ├── templates/
        │   ├── base.html
        │   └── core/
        │       └── item_list.html
        ├── urls.py
        ├── views.py
        └── tests.py

Importante: En la estructura anterior se muestra venv/ para documentar el entorno local, pero esta carpeta debe estar incluida en .gitignore y no debe subirse a GitHub.

10.4. Crear el repositorio Git

Desde la raíz del proyecto:

git init

Configurar el nombre de la rama principal:

git branch -M main

Agregar los archivos:

git add .

Crear el primer commit:

git commit -m "Proyecto inicial Django 5"

10.5. Crear el repositorio en GitHub

En GitHub crear un repositorio nuevo, por ejemplo:

django_project

Se recomienda crear el repositorio vacío para evitar conflictos iniciales con archivos generados automáticamente.

Después, conectar el repositorio remoto:

git remote add origin https://github.com/USUARIO/django_project.git

Reemplazar USUARIO por el nombre de usuario correspondiente.

Verificar el remoto:

git remote -v

Finalmente:

git push -u origin main

Uso de GitHub Copilot en Visual Studio Code

GitHub Copilot puede utilizarse como asistente durante el desarrollo, pero es importante revisar y comprender el código generado.

Algunos ejemplos de instrucciones que se pueden utilizar en Copilot Chat son:

Crea un modelo Django llamado Item con los campos name,
description y created_at siguiendo las convenciones de Django.

Explícame qué hace esta vista de Django y verifica si está
obteniendo correctamente todos los objetos Item.

Revisa este archivo settings.py y comprueba si la aplicación
core está registrada correctamente en INSTALLED_APPS.

Genera una plantilla Django que herede de base.html y muestre
una lista de objetos usando for y empty.

Revisa la estructura de mi proyecto Django y dime si cumple
con una separación entre src y config.

Copilot puede ayudar a generar código, explicar errores, proponer mejoras y crear pruebas, pero cada cambio debe ser revisado antes de aceptarlo.

Comandos principales utilizados

Objetivo

Comando

Crear carpeta

mkdir django_project

Crear entorno virtual

py -m venv venv

Activar entorno

.\venv\Scripts\Activate.ps1

Instalar Django 5

python -m pip install "Django>=5,<6"

Ver versión de Django

python -m django --version

Crear proyecto

django-admin startproject config .

Crear aplicación

python manage.py startapp core

Comprobar configuración

python manage.py check

Crear migraciones

python manage.py makemigrations

Aplicar migraciones

python manage.py migrate

Crear superusuario

python manage.py createsuperuser

Ejecutar servidor

python manage.py runserver

Generar dependencias

python -m pip freeze > requirements.txt

Inicializar Git

git init

Agregar archivos

git add .

Crear commit

git commit -m "Proyecto inicial Django 5"

Subir a GitHub

git push -u origin main

Instalación del proyecto desde cero

Si otra persona descarga el repositorio desde GitHub, puede realizar la instalación con los siguientes pasos.

1. Clonar el repositorio

git clone https://github.com/USUARIO/django_project.git
cd django_project

2. Crear el entorno virtual

py -m venv venv

3. Activar el entorno virtual

.\venv\Scripts\Activate.ps1

4. Instalar dependencias

python -m pip install -r requirements.txt

5. Entrar en src

cd src

6. Aplicar migraciones

python manage.py migrate

7. Crear superusuario

python manage.py createsuperuser

8. Ejecutar el servidor

python manage.py runserver

Después se puede acceder a:

http://127.0.0.1:8000/

y:

http://127.0.0.1:8000/admin/

Conclusión

Con estos ejercicios se construye una aplicación Django básica siguiendo una estructura organizada y adecuada para comenzar un proyecto web.

Se practican los principales componentes de Django:

Creación y administración de entornos virtuales.

Instalación de Django.

Estructuración de proyectos.

Creación de aplicaciones.

Modelos y migraciones.

Vistas.

URLs.

Plantillas.

Herencia de templates.

Panel de administración.

Creación de superusuarios.

Gestión de datos.

Dependencias mediante requirements.txt.

Control de versiones con Git.

Publicación del proyecto en GitHub.

Uso de GitHub Copilot como asistente de programación.

El resultado final es un proyecto funcional que puede utilizarse como base para continuar agregando funcionalidades, estilos, formularios, autenticación, pruebas y una API.