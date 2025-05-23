import os
from pathlib import Path
from decouple import config
from django.core.management.commands.runserver import Command as runserver


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "babysuite.m1293b.com",
]  # Update before launching with your own domain

runserver.default_port = "5000"
runserver.default_addr = "116.203.63.16"  # Update before launching on a new server

# Application definition
INSTALLED_APPS = [
    "home",
    "accounts",
    "cart",
    "orders",
    "products",
    "reviews",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    # The following apps are required for allauth:
    "allauth",
    "allauth.account",
    # Optional -- requires install using `django-allauth[socialaccount]`.
    "allauth.socialaccount",
    # ... include the providers you want to enable:
    "allauth.socialaccount.providers.amazon",
    "allauth.socialaccount.providers.apple",
    "allauth.socialaccount.providers.auth0",
    "allauth.socialaccount.providers.digitalocean",
    "allauth.socialaccount.providers.discord",
    "allauth.socialaccount.providers.gitea",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.gitlab",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.microsoft",
    "allauth.socialaccount.providers.nextcloud",
    "allauth.socialaccount.providers.paypal",
    "allauth.socialaccount.providers.reddit",
    "allauth.socialaccount.providers.snapchat",
    "allauth.socialaccount.providers.stripe",
    "allauth.socialaccount.providers.twitch",
    "allauth.socialaccount.providers.twitter",
    "allauth.socialaccount.providers.twitter_oauth2",
    "allauth.socialaccount.providers.yahoo",
    "tailwind",
    "theme",
    "fontawesomefree",
    "widget_tweaks",
]

if config("USE_AWS"):
    INSTALLED_APPS += [
        "storages",
    ]
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
    # AWS_S3_SIGNATURE_NAME = config("AWS_S3_SIGNATURE_NAME")
    AWS_S3_FILE_OWERSWRITE = False
    AWS_S3_CUSTOM_DOMAIN = (
        f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    )
    AWS_S3_VERITY = True
    DEFAULT_FILE_STORAGE = (
        "storages.backends.s3boto3.S3Boto3Storage"  # Use S3 storage for static files
    )


# # Media files configuration
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"  # URL path for media access
MEDIAFILES_STORAGE = "custom_storages.CustomMediaStorage"
MEDIA_ROOT = os.path.join(
    BASE_DIR, "media"
)  # Local filesystem path for storing media files
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"  # URL path for static files
STATICFILES_STORAGE = "custom_storages.CustomStaticStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]  # Additional locations of static files

STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
    "staticfiles": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
}

STATIC_ROOT = BASE_DIR / "staticfiles/"


TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = ["127.0.0.1"]
NPM_BIN_PATH = "/usr/bin/npm"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "babysuite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "babysuite.staticfiles_processor.static_urls",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # required by allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "babysuite.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),  # or your database server address
        "PORT": config("DB_PORT"),  # default PostgreSQL port is 5432
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CSRF_TRUSTED_ORIGINS = ["https://babysuite.m1293b.com"]

# Internationalization
LANGUAGE_CODE = "en-uk"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = config("EMAIL_HOST")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

# Stripe keys from .env file
FREE_DELIVERY_THRESHOLD = config("FREE_DELIVERY_THRESHOLD")
STANDARD_DELIVERY_PERCENTAGE = config("STRIPE_STANDARD_DELIVERY_PERCENTAGE")
# STRIPE_PRICE_ID = config("STRIPE_PRICE_ID")
STRIPE_DEFAULT_CURRENCY = "gbp"
# STRIPE_CHECKOUT_SESSION_ID = config("STRIPE_CHECKOUT_SESSION_ID")
# STRIPE_SUCCESS_URL = config("STRIPE_SUCCESS_URL")
# STRIPE_CANCEL_URL = config("STRIPE_CANCEL_URL")
# STRIPE_CHECKOUT_SESSION_URL = config("STRIPE_CHECKOUT_SESSION_URL")
# STRIPE_SESSION_ID = config("STRIPE_SESSION_ID")
# STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY")
