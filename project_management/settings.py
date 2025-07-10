INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
