"""
Django settings for the "core" project.

https://docs.djangoproject.com/en/4.2/topics/settings
https://docs.djangoproject.com/en/4.2/ref/settings
https://django-debug-toolbar.readthedocs.io/en/latest/index.html
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4*znbb7y8a(vhe#m&^%f390!(*oeizzbf062gk04+s7l=of61b"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Allowed hosts
ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    '192.168.43.198',
    '.example.com',
]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "widget_tweaks",
    "apps.accounts",
    "apps.assets",
    "apps.gatepasses",
]


# Warning: The order of MIDDLEWARE is important when using django-debug-toolbar. You 
# should include its middleware as early as possible in the list. However, it must come 
# after any other middleware that encodes the response’s content, such as GZipMiddleware.
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware", 
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


ROOT_URLCONF = "core.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files

STATIC_URL = "static/"

STATICFILES_DIRS = (
    BASE_DIR / "apps/accounts/static/",
    BASE_DIR / "apps/assets/static/",
    BASE_DIR / "apps/gatepasses/static/",
)

STATIC_ROOT = BASE_DIR / "staticroot/"


# Media files
# MEDIA_URL is the URL we can use in our templates for the files

MEDIA_URL = '/media/'

# MEDIA_ROOT is the absolute filesystem path to the directory for user-uploaded files
MEDIA_ROOT = BASE_DIR / "media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SITE_ID = 1


AUTH_USER_MODEL = 'accounts.Account'


LOGIN_REDIRECT_URL = 'accounts_home'
LOGOUT_REDIRECT_URL = 'accounts_home'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}


# The django-debug-toolbar is shown only if your IP address is listed in Django's 
# INTERNAL_IPS setting.
# https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-INTERNAL_IPS
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html
INTERNAL_IPS = [
    "127.0.0.1",
    '0.0.0.0',
    '192.168.43.198',
]
