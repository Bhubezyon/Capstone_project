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
