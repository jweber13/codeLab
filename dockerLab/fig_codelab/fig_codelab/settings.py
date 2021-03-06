"""
Django settings for fig_codelab project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p_n*x(_^$yr1!5*k6+%#zx^9hncx+44$h95tbx+u6f*zns_vrs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fig_codelab.urls'

WSGI_APPLICATION = 'fig_codelab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#import dj_database_url
#DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'default_db',
#	'USER': '',
#	'PASSWORD': '',
#	'HOST': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
#    ...
    'formatters': {
        'loggly': {
            'format':'loggly: %(message)s',
        },
    },
    'handlers': {
#        ...
        'logging.handlers.SysLogHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local5',
            'formatter': 'loggly',
        },
    },
    'loggers': {
#        ...
        'loggly_logs':{
            'handlers': ['logging.handlers.SysLogHandler'],
            'propagate': True,
            'format':'loggly: %(message)s',
            'level': 'DEBUG',
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY', '')
#AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_STORAGE_BUCKET_NAME = 'codelabjw'
AWS_QUERYSTRING_AUTH = False
#S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = 'http://codelabjw.s3.amazonaws.com'
#STATIC_URL=path.join(PROJECT_ROOT, 'static')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
