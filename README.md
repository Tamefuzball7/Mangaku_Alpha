
1. Clona el repositorio o descargalo como zip.

```git clone https://github.com/mundo-python/social_project.git```


2. Crea un ambiente virtual 

```python -m venv socialenv```


3. Instala las dependencias/librerias en requirements.txt

```pip install -r requirements.txt```
`

4. Remplazar la base de datos 
```remplazar los datos por la base de datos que vas a usar en el archivo settings.py, recuerda que es una base de datos PostgreSQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '202001',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ,
        },
    }
}

```

5. Ejecuta las migraciones.

```python manage.py makemigrations```
```python manage.py migrate```

6. Crea un superusuario.

```python manage.py createsuperuser```

7. Corre el servidor.

```python manage.py runserver```

