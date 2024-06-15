import sys

from django.conf.urls import url
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from django.views.generic import View

from cuser.middleware import CuserMiddleware
from .models import TestModel, TestModel2


User = get_user_model()


class TestCUserView(View):
    def get(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        return HttpResponse(user and user.username or "")

class CuserTestCase(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="test"
        )

    def test_cuser_middleware(self):
        request = self.factory.get("/test-view/")
        response = TestCUserView.as_view()(request)

        if sys.version < '3':
            self.assertEqual(response.content, "")
        else:
            self.assertEqual(response.content, b"")

        self.client.login(username="test", password="test")
        response = self.client.get(reverse('test-view'))

        if sys.version < '3':
            self.assertEqual(response.content, "test")
        else:
            self.assertEqual(response.content, b"test")

    def test_current_user_field(self):
        user = User.objects.get(username="test")
        CuserMiddleware.set_user(user)
        TestModel.objects.create(name="TEST")
        CuserMiddleware.del_user()
        test_instance = TestModel.objects.get(name="TEST")

        self.assertEqual(test_instance.creator, user)

    def test_current_user_field_with_no_active_user(self):
        CuserMiddleware.del_user()
        TestModel.objects.create(name="TEST")
        test_instance = TestModel.objects.get(name="TEST")

        self.assertEqual(test_instance.creator, None)
