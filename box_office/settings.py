import django_heroku
import os
from decouple import config
import dj_database_url

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ISLOCAL = config('ISLOCAL', cast=bool)

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '.herokuapp.com',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/media/'

STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/static/'

COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
COMPRESS_OFFLINE = True


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mraduldubeymd19@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxxx'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'home'

SITE_ID=1

#Paypal vals
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = EMAIL_HOST


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',                                                                 
    'allauth.account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.forms',
    'crispy_forms',
    'djmoney',
    'blog',
    'booking',
    'contact',
    'players',
    'paypal.standard.ipn',
    'social_django',
    'markdownx',
    'users.apps.UsersConfig',
]

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'box_office.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #required for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

#For allauth:
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


WSGI_APPLICATION = 'box_office.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


#if ISLOCAL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#else:
#   db_from_env = dj_database_url.config(conn_max_age=600)
    #DATABASES = {'default': None}
#    DATABASES['default'].update(db_from_env)


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

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#For offline testing we used static folder outside the BASE_DIR
'''
if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static","static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static","media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR),"static","static"),
    )
'''
#template packs of crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Social Django
SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

# Activate Django-Heroku.
django_heroku.settings(locals())
