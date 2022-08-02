from http import HTTPStatus

from django.test import Client, TestCase


class HelloPageTest(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.name = 'test'
        self.message = 'test message'

    def test_main_url_exists_at_desired_location(self):
        """Проверка доступности адреса главной страницы."""
        response = self.guest_client.get('/?name={name}&message={message}')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_author_url_uses_correct_template(self):
        """Проверка шаблона для главной страницы."""
        response = self.guest_client.get('')
        self.assertTemplateUsed(response, 'hello/main.html')


class ViewTestClass(TestCase):
    def test_error_page(self):
        """Проверка доступности  кастомной страницы 404."""
        response = self.client.get('/nonexist-page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_error_page_template(self):
        """Проверка  шаблона кастомной страницы 404."""
        response = self.client.get('/nonexist-page/')
        self.assertTemplateUsed(response, 'erors_pages/404.html')
