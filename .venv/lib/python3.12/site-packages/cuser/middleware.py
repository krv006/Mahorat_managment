from __future__ import unicode_literals
import threading
from cuser.compat import User

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    # Works perfectly for everyone using MIDDLEWARE_CLASSES
    MiddlewareMixin = object


class CuserMiddleware(MiddlewareMixin):
    """
    Always have access to the current user
    """
    __users = {}

    def process_request(self, request):
        """
        Store user info
        """
        self.__class__.set_user(request.user)

    def process_response(self, request, response):
        """
        Delete user info
        """
        self.__class__.del_user()
        return response

    def process_exception(self, request, exception):
        """
        Delete user info
        """
        self.__class__.del_user()

    @classmethod
    def get_user(cls, default=None):
        """
        Retrieve user info
        """
        return cls.__users.get(threading.current_thread(), default)

    @classmethod
    def set_user(cls, user):
        """
        Store user info
        """
        if isinstance(user, str):
            user = User.objects.get(username=user)
        cls.__users[threading.current_thread()] = user

    @classmethod
    def del_user(cls):
        """
        Delete user info
        """
        cls.__users.pop(threading.current_thread(), None)
