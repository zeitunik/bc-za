"""Base test cases."""
import django_functest
from django import test
from django.contrib.staticfiles import testing as static_testing


class WebTestBase(django_functest.FuncWebTestMixin, test.TestCase):
    """Base class for web client tests that don't require javascript."""

    def setUp(self):
        super().setUp()


class SeleniumTestBase(django_functest.FuncSeleniumMixin, static_testing.StaticLiveServerTestCase):
    """Base class for browser tests."""

    driver_name = "Firefox"
