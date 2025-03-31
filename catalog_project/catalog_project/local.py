from settings import DATABASES,BASE_DIR
from settings import TEMPLATES  

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / "db.sqlite3",
}

DEBUG = True
INTERNAL_IPS = ('127.0.0.1', 'localhost')
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})
ALLOWED_HOSTS = ['*']

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ****************************************************************
# THIRD-PARTY


# DEBUG
DEBUG = True
ALLOWED_HOSTS = ['*']
