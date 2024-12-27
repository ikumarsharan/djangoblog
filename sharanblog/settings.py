from pathlib import Path
import os
from django.conf import settings
# from . info import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#SIte ID
# SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = 'SHARAN KUMAR BLOG <i.kumar.sharan@gmail.com>'
EMAIL_HOST_USER = 'i.kumar.sharan@gmail.com'
EMAIL_HOST_PASSWORD = 'padttbdzsxizibdp'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 600
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-be6f=55%2yo5=of6lcwshmchaw-_@gh4j$65&!s5^*^3=oei0#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

RECAPTCHA_SECRET = getattr(settings, "RECAPTCHA_SECRET", '6Lf8HqYqAAAAACfSZTuJmhrzsIflGK7KJu3ggSkk')
RECAPTCHA_KEY = getattr(settings, "RECAPTCHA_KEY", '6Lf8HqYqAAAAAIOCY6Tiym0I76J_DxZT55PdJESR')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoblog',
    'members',
    'tinymce',
    'django_summernote',
    'crispy_forms',
    'captcha',
    'django_email_verification',
    'django_user_agents',
    'social_django',
    'category',
    'django.contrib.sites',
]

SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

CRISPY_TEMPLATE_PACK = 'uni_form'

HCAPTCHA_SITEKEY = '49a228af-fac4-42c7-9ea3-0f6d01c40bf2'
HCAPTCHA_SECRET = '0x90b678cB8976455dd943A5971aea2D0463cF6188'

# RECAPTCHA_PUBLIC_KEY = '6Lfwc3UkAAAAAOC-eZnu2ukzMfsKkcM0wESttm1d'
# RECAPTCHA_PRIVATE_KEY = '6Lfwc3UkAAAAABU5ZSg4LKhJRr1A8uMhTtchv8x7'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'ipinfo_django.middleware.IPinfoMiddleware',
]

ROOT_URLCONF = 'sharanblog.urls'

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
                # Add the following two
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'sharanblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          'NAME': 'djangosharan',
#          'USER': 'sharani',
#          'PASSWORD': 'Sharan1212@',
#          'HOST':'68.178.145.146',
#          'PORT':'3306',
#      }
#  }

# localhost database

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
       'NAME': 'djangosharan',
       'USER': 'root',
       'PASSWORD': '',
      'HOST':'127.0.0.1',
      'PORT':'3306',
      "OPTIONS": {
        "init_command": "SET default_storage_engine=INNODB",
    }
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     'D:\django-blog\static',
# ]
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# social auth configs for google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '336947511925-46qqbk799dctbfgg77sue52502otut6g.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
