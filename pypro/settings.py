"""
Django settings for pypro project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import json

#sudo chown -R :www-data pypro/media/
#sudo chmod -R 775 pypro/media

with open('/Users/omidsoroush/Desktop/config/config.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '49.12.203.203', 'www.datasciencetutorials.org', 'datasciencetutorials.org']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'blog.apps.BlogConfig',
    'pytutorial.apps.PytutorialConfig',
    'users.apps.UsersConfig',
    'sendemail',
    'crispy_forms',
    'tinymce',
    'storages',
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

ROOT_URLCONF = 'pypro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'pypro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pypro_db',
        'USER': 'postgres',
        'PASSWORD': config['DB_PASS'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_REDIRECT_URL = 'blog:blog-home'
LOGIN_URL = 'login'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'content_css': "/static/blog/tinymce/tinypage.css",
    'theme': 'silver',
    'file_picker_types': 'file image media',
    'images_upload_url': '/upload_image/',
    'height': 700,
    'plugins': '''
            textcolor save link image imageupload media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak spellchecker
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor h3 h4 h5 h6 | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |removeformat
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'nonbreaking_force_tab': True,
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'},
        {'text': 'none', 'value': 'none‚'},
        {'text':"r",'value':"r"},
        {'text': 'HTML/XML', 'value': 'markup'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'PHP', 'value': 'php'},
        {'text': 'Ruby', 'value': 'ruby'},
        {'text': 'Java', 'value': 'java'},
        {'text':"d",'value':"d"},
        {'text':"dart",'value':"dart"},
        {'text':"diff",'value':"diff"},
        {'text':"docker",'value':"docker"},
        {'text':"eiffel",'value':"eiffel"},
        {'text':"elixir",'value':"elixir"},
        {'text':"erlang",'value':"erlang"},
        {'text':"fsharp",'value':"fsharp"},
        {'text':"fortran",'value':"fortran"},
        {'text':"git",'value':"git"},
        {'text':"glsl",'value':"glsl"},
        {'text':"go",'value':"go"},
        {'text':"groovy",'value':"groovy"},
        {'text':"haml",'value':"haml"},
        {'text':"handlebars",'value':"handlebars"},
        {'text':"haskell",'value':"haskell"},
        {'text':"haxe",'value':"haxe"},
        {'text':"http",'value':"http"}
    ]
}



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email section
# config/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
# EMAIL_HOST = 'securesmtp.t-online.de'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = config.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')


AWS_ACCESS_KEY_ID = config.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
