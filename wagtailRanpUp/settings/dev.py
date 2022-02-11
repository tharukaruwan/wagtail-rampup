from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$gw7k=pqt@wh^p5r)#z+z729e*mk6nck!y1%&l5mbu+im@o1c9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    # "django.contrib.staticfiles",   # not nessory because base.py has
    "debug_toolbar",
]

MIDDLEWARE = MIDDLEWARE + [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# STATIC_URL = "static/" # not nessory because in base.py STATIC_URL = '/static/'

try:
    from .local import *
except ImportError:
    pass
