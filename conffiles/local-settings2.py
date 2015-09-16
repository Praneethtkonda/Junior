# Local settings for Django projects
# Set all values here before starting the project
# Move this file to the same folder as main settings.py file
# Rename the file as local_settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

ADMINS = (
        ('Seshagiri Prabhu', 'seshagiriprabhu@gmail.com'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Registration mail settings

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'inctf.in@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Junior InCTF Portal <contact@inctf.in>'
ADMINS_EMAIL = map(lambda x: x[1], ADMINS)
MANAGERS = ADMINS

# If running in debug mode, write emails to files.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ['junior.inctf.in']

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '!#sd2=qwqr1sbgob91%icu8_ijas*ukov-hxc%wu0n6n_uah0)'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Cache backend.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"


# NoCaptcha ReCaptcha settings

RECAPTCHA_PUBLIC_KEY = '6LdbfwwTAAAAALo-K7eTHeg8V3Uizpm--XIhmCy4'
RECAPTCHA_PRIVATE_KEY = '6LdbfwwTAAAAAPchjz23QjllJprbHp7lSfjkyRcn'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

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
