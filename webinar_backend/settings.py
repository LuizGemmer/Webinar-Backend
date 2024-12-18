"""
Django settings for webinar_backend project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1", ".vercel.app", "localhost"
]

AUTH_USER_MODEL = 'user.User'

SITE_ID = 1

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "SIGNIN_KEY": "updateme",
    "ALGORITHM": "HS512"
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [(
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    )],
    "DEFAULT_PERMISSION_CLASSES": [(
        "rest_framework.permissions.IsAuthenticated"
    )],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CORS_ALLOWED_ORIGINS = [
    'https://127.0.0.1:8000',
    'https://127.0.0.1:3000'
]

REST_AUTH = {
    "USE_JWT": True,
    'JWT_AUTH_HTTPONLY': False
}

# Application definition

INSTALLED_APPS = [
    ## Default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## Rest framework apps and auth
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',

    ## Swagger
    'drf_spectacular',

    'storages',

    ## Custom Apps
    'user.apps.UserConfig',
    'courses.apps.CoursesConfig',
    'permissions.apps.PermissionsConfig',
    'quiz.apps.QuizConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webinar_backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'webinar_backend.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DATABASE'), 
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'), 
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static'

# MEDIA_URL = os.environ.get('MEDIA_URL')
# MEDIA_ROOT = MEDIA_URL + "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN = "admin"
SUPERVISOR = "supervisor"
MANAGER = "manager"
VIEWER = "viewer"

USER_PERMISSION_CHOICES = {
        ADMIN: "admin",
        SUPERVISOR: "supervisor",
        MANAGER: "manager",
        VIEWER: "viewer",
    }

USER_PERMISSION_CONFIG = {
    ADMIN: {
        "code": ADMIN
        , "can_edit": True
        , "can_create": True
        , "can_delete": True
        , "can_view_own_items": True
        , "can_view_all_items": True
        , "can_set_viewer_permissions": True
        , "can_set_higher_permissions": True
    },
    SUPERVISOR: {
        "code": SUPERVISOR
        , "can_edit": True
        , "can_create": True
        , "can_delete": True
        , "can_view_own_items": True
        , "can_view_all_items": True
        , "can_set_viewer_permissions": True
        , "can_set_higher_permissions": False
    },
    MANAGER: {
        "code": VIEWER
        , "can_edit": False
        , "can_create": False
        , "can_delete": False
        , "can_view_own_items": True
        , "can_view_all_items": True
        , "can_set_viewer_permissions": False
        , "can_set_higher_permissions": False
    },
    VIEWER: {
        "code": "admin"
        , "can_edit": False
        , "can_create": False
        , "can_delete": False
        , "can_view_own_items": True
        , "can_view_all_items": False
        , "can_set_viewer_permissions": False
        , "can_set_higher_permissions": False
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Webinar API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

QUIZ_RELATED_CLASS_MODEL = "permissions.Function"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'ruisu-webinar-bucket'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        'BACKEND': "storages.backends.s3.S3Storage"
    }
}



