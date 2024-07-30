from django.test import TestCase
from django.test.utils import override_settings


class HomeTestCase(TestCase):
    # Replaced by "--debug-mode" in test command
    # @override_settings(DEBUG=True)
    def test_home_page(self):
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 301, 302])


class AdminTestCase(TestCase):
    # Replaced by "--debug-mode" in test command
    # @override_settings(DEBUG=True)
    def test_admin_page(self):
        response = self.client.get("/admin")
        self.assertIn(response.status_code, [200, 301, 302])
