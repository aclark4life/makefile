from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9u#j8fvxq1c397jj17np#!o==7+!3e4f(cq-32hc8f(!*7e#2!"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
MIDDLEWARE.append('hijack.middleware.HijackUserMiddleware')
INTERNAL_IPS = ["127.0.0.1",]
