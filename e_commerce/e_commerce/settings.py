"""
Django settings for e_commerce project.

Generated by 'django-admin startproject' using Django 3.2.18

"""

from pathlib import Path
import os
from cryptography.fernet import Fernet
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Agregado para no tener que crea el archivo env a mano
file = Path(os.path.join(BASE_DIR, '.env'))
if not file.exists():
    SECRET_KEY = Fernet.generate_key()
    archkey = open(os.path.join(BASE_DIR, '.env'), 'w')
    archkey.writelines(f'# Clave secreta de la App')
    archkey.writelines(f'\nSECRET_KEY={SECRET_KEY}')
    # BASE DE DATOS
    archkey.writelines(f'\n')
    archkey.writelines(f'\n#DATABASE')
    archkey.writelines(f'\nENGINE=')
    archkey.writelines(f'\nDATABASE=')
    archkey.writelines(f'\nUSERDB=')
    archkey.writelines(f'\nPASSWORDDB=')
    archkey.writelines(f'\nHOST=')
    archkey.writelines(f'\nPORT=')
    # EMAIL
    archkey.writelines(f'\n')
    archkey.writelines(f'\n#CORREO')
    archkey.writelines(f'\nENGINE=')
    archkey.writelines(f'\nDATABASE=')
    archkey.writelines(f'\nUSERDB=')
    archkey.writelines(f'\nPASSWORDDB=')
    archkey.writelines(f'\nHOST=')
    archkey.writelines(f'\nPORT=')
    archkey.close()
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY=env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home', 'carrito', 'pedidos', 'productos', 'userApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'e_commerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'e_commerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),   # Cadena del motor 'django.db.backends.postgresql'
        'NAME': env('DATABASE'),        # Nombre de la Base de Datos 
        'USER': env('USERDB'),       # Usuario de la Base de Datos 
        'PASSWORD': env('PASSWORDDB'),    # Contraseña del Usuario
        'HOST': env('HOST'),            # Nombre del Host o IP donde esta ejecutandose el servidor
        'PORT': env('PORT'),            # Puerto al cual se debe conectar
    }
}

print(DATABASES)
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

#El debug true, buscar un directorio static dentro del proyecto
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Limpieza de la pantalla despues de una modificacion
import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#Configuracion para el envio de email por medio de GMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# Clave generada desde la configuracion de Google
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")

# Redireccion de LOGIN para que no de error 404
LOGIN_REDIRECT_URL = 'index'