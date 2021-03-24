"""
Django settings for Diet project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MY_SITE_URL = 'https://communitygis.net/'
TIME_INPUT_FORMATS = ['%I:%M %p']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7po=w($if%^)(rthq9qvrgda=+!93oo2l+8qt3$_$f&jlh&uoh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dietdiversity.communitygis.net','*']

BOOTSTRAP4 = {
    'include_jquery': True,
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DemoDiet',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'crispy_forms',
    'modelcluster',
    'taggit',
    'Diet',
    'CMSResources',
    'import_export',
    'django.contrib.gis',
    'base',
    'login',
    'registration',
    'resources',
    'data_feed',
    'bootstrap_datepicker_plus',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'Diet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

            ],
        },
    },
]

WSGI_APPLICATION = 'Diet.wsgi.application'

ENCRYPT_KEY=b'e6P0yF7QPoszzM1FmMrfKs8yPDZ1OAHl-jhHRDYpD6g='
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'c_diet',
        'USER' : 'postgres',
        'PASSWORD' : 'postgres',
        'HOST': 'localhost',
         'PORT':'5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOCALE_PATHS =[
    os.path.join(BASE_DIR,'locale'),
    

]

LANGUAGES =[
    ('en', 'English'),
    ('hi','Hindi'),
    ('mr', 'Marathi')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER="communitygis.dietdiversity@gmail.com"
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=465
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD= "cdd@2021"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
# SESSION_EXPIRE_SECONDS = 8*60*60  # 1 hour

# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

# SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 2 # group by minute

# SESSION_TIMEOUT_REDIRECT = '/logout/'
WAGTAIL_SITE_NAME = 'Diet Diversity Website'




