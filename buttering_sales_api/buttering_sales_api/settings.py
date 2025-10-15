import os

# Templates
TEMPLATES[0]['DIR'] = [os.path.join(BASE_DIR, 'templates')]

# Static files
STATIC.URL = '/static/'
STATICFILES.DIR = [os.path.join(BASE_DIR, 'static')]

# Media files (for image uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'

INSTALLED_APPS += [
    'rest_framework',
    'restframe_.authtoken',
    'sales',
    'posts'
]
AUTH_USER_MODEL = 'sales.Custom.User'

REST_FRAMEWORK = {
    'DEFAULT_PEGINATION_CLASSES': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
}

# SECURITY FEATURES
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
 
