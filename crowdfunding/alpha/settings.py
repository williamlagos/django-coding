import os

DEBUG = True

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_DATE = ("Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez")

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.abspath('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.abspath('alpha/public')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath('static'),
            os.path.abspath('alpha/templates/pug'),
            os.path.abspath('alpha/templates')
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': ['pypugjs.ext.django.templatetags'],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'alpha.urls'
WSGI_APPLICATION = 'alpha.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pure_pagination',
    'crispy_forms',
    'socialize',
    'shipping',
    'feedly',
    'django_distill'
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'efforia.Profile'

EFFORIA_APPS = ()
EFFORIA_OBJS = {}
EFFORIA_NAMES = {}
EFFORIA_TOKENS = {}
EFFORIA_URL = ''

ADMINS = (('William Oliveira de Lagos', 'william@efforia.com.br'),)
MANAGERS = ADMINS
SECRET_KEY = 'x5dvfbk$u-(07^f1229p*_%rcuc+nka45j6awo==*jkyjiucql'

#DATABASES = {
#  'default': {
#    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#    'NAME': 'd6i6a0klirtqjd',
#    'HOST': 'ec2-54-243-243-176.compute-1.amazonaws.com',
#    'PORT': 5432,
#    'USER': 'kkoaphemdgvutt',
#    'PASSWORD': 'ztTIw8EcIYX2UlNolrVmTb8yZQ'
#  }
#}

DATABASES = {
  'default': {
    'ENGINE':'django.db.backends.sqlite3',
    'NAME':'alpha.db',
  }
}

PAYPAL_RECEIVER_EMAIL = 'efforiaca@gmail.com'
PAYPAL_NOTIFY_URL = '/paypal'
PAYPAL_RETURN_URL = '/'
PAYPAL_CANCEL_RETURN = '/cancel'

PAGSEGURO_EMAIL_COBRANCA = 'contato@efforia.com.br'
PAGSEGURO_TOKEN = '1a3ea7wq2e7eq8e1e223add23ad23'
PAGSEGURO_URL_RETORNO = '/pagseguro/retorno/'
PAGSEGURO_URL_FINAL = '/obrigado/'
PAGSEGURO_ERRO_LOG  = '/tmp/pagseguro_erro.log'

EFFORIA_APPS = ['alpha']
EFFORIA_ACTIONS = {'alpha':[]}
EFFORIA_OBJS = { 'alpha': ['Project','Event'] }
EFFORIA_NAMES = { 'alpha': ('Promova','alpha') }
EFFORIA_TOKENS = {
    "@": "efforia.Profile",
    "!#":"efforia.Page",
    "#": "alpha.Project",
    "@#":"alpha.Project",
    "##":"alpha.Movement",
    "@!":"alpha.Event",
    "@": "alpha.Event",
    "@@":"alpha.Event"
}
EFFORIA_URL = 'promova.co'

STATICFILES_DIRS.extend([ os.path.abspath('alpha/public') ])

INSTALLED_APPS.extend(EFFORIA_APPS)

ALLOWED_HOSTS = ['*',]
