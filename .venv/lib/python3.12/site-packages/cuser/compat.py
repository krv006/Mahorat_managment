from __future__ import unicode_literals
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import django
from django.utils.functional import lazy

__all__ = ['User', 'AUTH_USER_MODEL']


# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
    try:
        from django.contrib.auth import get_user_model
        User = lazy(get_user_model, AUTH_USER_MODEL)
    except ImproperlyConfigured:
        pass
else:
    from django.contrib.auth.models import User
    AUTH_USER_MODEL = 'auth.User'
