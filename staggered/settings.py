# Django settings for staggered project.
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a@erzcvm3&9xasn779-i(9&lrmm#vey5mmyz5)us9=5b8&12=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.herokuapp.com'
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'axes',
    'reversion',
    'rest_framework',
    'rest_framework.authtoken',
    'compressor',
    'plugins.staggered_theme',
    'opal',
    'opal.core.search',
    'opal.core.pathway',
    'opal.core.referencedata',
    'staggered',
    'django.contrib.admin',
]

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'opal.middleware.AngularCSRFRename',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'opal.middleware.DjangoReversionWorkaround',
    'reversion.middleware.RevisionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'staggered.urls'
APPEND_SLASH = False

LOADERS = [(
                # TODO: Django 1.11 makes turns this loader on by default, so
                # this section and `debug` can be removed then.
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            )]
if DEBUG:
    LOADERS = (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'opal.context_processors.settings',
                'opal.context_processors.models',
                'opal.core.pathway.context_processors.pathways',
            ],
            'loaders': LOADERS
        },
    },
]

WSGI_APPLICATION = 'staggered.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
try:
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(default='sqlite:///' + PROJECT_PATH + '/opal.sqlite')
    }
except ImportError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_PATH, 'opal.sqlite'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': ''
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'assets')
STATICFILES_DIRS = [
    os.path.join(PROJECT_PATH, 'static'),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Django Site identifier
SITE_ID = 1

# Date and Time Formatting
# https://docs.djangoproject.com/en/1.10/ref/settings/#date-format
DATETIME_FORMAT = 'd/m/Y H:i:s'
DATETIME_INPUT_FORMATS = ['%d/%m/%Y %H:%M:%S']
DATE_FORMAT = 'd/m/Y'
DATE_DISPLAY_FORMAT = 'D MMM YYYY'
DATE_INPUT_FORMATS = ['%d/%m/%Y']
TIME_FORMAT = "H:i:s"


# Emails
# https://docs.djangoproject.com/en/1.10/ref/settings/#email-backend
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
if not DEBUG:
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
else:
    EMAIL_PORT = 1025
    EMAIL_HOST = 'localhost'


# HTTPS support
# https://docs.djangoproject.com/en/1.10/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Sessions
# https://docs.djangoproject.com/en/1.10/topics/http/sessions/#browser-length-sessions-vs-persistent-sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# CSRF
# https://docs.djangoproject.com/en/1.10/ref/settings/#csrf-cookie-name
CSRF_COOKIE_NAME = 'XSRF-TOKEN'
CSRF_FAILURE_VIEW = 'opal.views.csrf_failure'


# ========== THIRD PARTY ==========
# Django Axes
AXES_LOCK_OUT_AT_FAILURE = False


# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


# ========== OPAL ==========
# Testing
COVERAGE_EXCLUDE_MODULES = (
    'staggered.migrations',
    'staggered.tests',
    'staggered.local_settings',
    'opal.migrations',
    'opal.tests',
    'opal.wsgi',
)

OPAL_LOG_OUT_MINUTES = 15
OPAL_LOG_OUT_DURATION = OPAL_LOG_OUT_MINUTES*60*1000

# OPAL_EXTRA_HEADER = ''
# OPAL_EXTRA_APPLICATION = ''

# Uncomment this if you want to swap the logo used by this application.
# http://opal.openhealthcare.org.uk/docs/v0.10.0/reference/settings/#opal_logo_path
# OPAL_LOGO_PATH = 'img/ohc-trans.png'

# Enable/Disable autocomplete from navbar search
OPAL_AUTOCOMPLETE_SEARCH = False

INTEGRATING = False

# OPAL-required Django settings you should edit
CONTACT_EMAIL = []
DEFAULT_FROM_EMAIL = 'hello@example.com'
DEFAULT_DOMAIN = 'http://staggered.com/'


# ========== PROJECT ==========
OPAL_BRAND_NAME = 'Staggered'
VERSION_NUMBER  = '0.1'

# if you want sass, uncomment the below and gem install sass
# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'sass --scss {infile} {outfile}'),
# )

try:
    from local_settings import *
except ImportError:
    pass
