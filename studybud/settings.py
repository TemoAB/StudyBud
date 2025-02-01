from pathlib import Path
import dj_database_url  # Import dj-database-url
import environ

# Initialise environment variables
env = environ.Env()

# Reading .env file
environ.Env.read_env()

ENVIRONMENT = env('ENVIRONMENT', default='production')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'studybud-temo.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://studybud-temo.up.railway.app']  # Fixed the typo here

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'admin_honeypot',
    'base.apps.BaseConfig',

    'rest_framework',
    "corsheaders",
]

AUTH_USER_MODEL = 'base.User'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise Middleware added here
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studybud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'studybud.wsgi.application'

# Database settings (default to SQLite if not in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES_LOCALLY = False
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY:
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'

# Configure WhiteNoise for serving static files in production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
if ENVIRONMENT == 'development':
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = ['https://studybud-temo.up.railway.app']  # restrict CORS to your production domain

# CSRF Cookie and Session Cookie settings for production
if ENVIRONMENT == 'production':
    CSRF_COOKIE_SECURE = True  # Only transmit cookies over HTTPS
    SESSION_COOKIE_SECURE = True  # Only transmit cookies over HTTPS
    SECURE_SSL_REDIRECT = False  # Redirect all HTTP to HTTPS
    CSRF_COOKIE_HTTPONLY = True  # Protect CSRF cookie from being accessed by JavaScript
    SESSION_COOKIE_HTTPONLY = True  # Protect session cookie from being accessed by JavaScript
