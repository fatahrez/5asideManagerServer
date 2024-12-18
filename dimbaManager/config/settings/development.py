from .base import *

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:4200',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ethereal.email'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # Use TLS for security
EMAIL_HOST_USER = 'sim.kohler71@ethereal.email'  # Your email address
EMAIL_HOST_PASSWORD = 'UcT2R4RBQRpz3z3kMF'  # Your email password (or app-specific password)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}