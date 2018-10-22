from .settings import INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo_companies',
        'USER': 'db_manager',
        'PASSWORD': '1qa2ws3ed',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTALLED_APPS += ['django_extensions']
