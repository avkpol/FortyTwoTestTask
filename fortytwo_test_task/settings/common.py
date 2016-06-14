"""
Django settings for fortytwo_test_task project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
os.environ["DJANGO_SETTINGS_MODULE"] = 'fortytwo_test_task.settings.common'


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.common'

# App/Library Paths
sys.path.append(os.path.join(BASE_DIR, 'fortytwo_test_task'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x=c0_e(onjn^80irdy2c221#)2t^qi&6yrc$31i(&ti*_jf3l8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',


    'crispy_forms',
    'avkpol4',
    'south',
)

SITE_ID = 1
LOGIN_URL ='/account/login/'
LOGIN_REDIRECT_URL = '/edit'

ACCOUNT_AUTHENTICATION_METHOD = "username_email" #(="username" | "email" | "username_email")
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # (=False)
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =  LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 10
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None #choices are: "mandatory", "optional", or None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject is: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" #if secure use https
ACCOUNT_LOGOUT_ON_GET = False #log user out right away.
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_SIGNUP_FORM_CLASS =None # add a custom sign up form
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True # use False if you don't want double password fields
ACCOUNT_UNIQUE_EMAIL= True #enforces emails are unique to all accounts
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username" # If you're using a Custom Model, maybe it's "email"
ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
#ACCOUNT_USER_DISPLAY (=a callable returning user.username)
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USERNAME_BLACKLIST =['some_username_youdon\'t_want']
ACCOUNT_USERNAME_REQUIRED =True #do you want them to have a user name?
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False #don't show the password
ACCOUNT_PASSWORD_MIN_LENGTH =6 #min length of password
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True #login the user after confirming email, if required.


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    # custom middleware to collect http requests
    'avkpol4.custom_middleware.SaveRequestDb',
)

TEMPLATE_CONTEXT_PROCESSORS = (

    # Required by `allauth` template tags
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',

)

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'fortytwo_test_task.urls'

WSGI_APPLICATION = 'fortytwo_test_task.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Upload Media
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static','media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")



STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)


# Template Settings
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)
#
# Turn off south during test
SOUTH_TESTS_MIGRATE = False
#
# # FIXTURE_DIRS = (
# #     os.path.join(BASE_DIR, 'mydata.json'),
# # )

