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