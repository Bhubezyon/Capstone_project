import os
from pathlib import Path
import django_database_urls

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes'
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'posts',
        'sales'
    ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

AUTHOR_USER_MODEL = 'users.CustomUser'

DEBUG = True
ALLOWED_HOSTS = [''] # DOMAIN PRODUCTION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'

    }
}

SIMPLE_JWT = {
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True
}

INSTALLED_APPS += ['csp']
MIDDLEWARE.insert(0, 'csp.middleware.CSPMiddleware')

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SCR = ("'self'", 'https://trusted.cdn.com')

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True