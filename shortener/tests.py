from django.test import TestCase
from shortener.models import Url


class UrlModelTestCase(TestCase):
    def setUp(self):
        url_google = Url.objects.create(url='https://google.com')
        url_y = Url.objects.create(url='https://y.ru')

        self.hash_google = url_google.url_hash
        self.hash_y = url_y.url_hash

    def test_get_non_exist_short_url(self):
        with self.assertRaises(Url.DoesNotExist):
            Url.objects.get(url_hash='none_exist_url_hash')

    def test_get_exist_short_url(self):
        self.assertEqual(Url.objects.get(url='https://google.com').url_hash, self.hash_google)

    def test_create_short_url(self):
        url_mail = Url.objects.create(url='http://mail.ru/')
        self.assertEqual(url_mail.url_hash, Url.objects.get(url='http://mail.ru/').url_hash)


class UrlViewTestCase(TestCase):
    def setUp(self):
        url_google = Url.objects.create(url='https://google.com')
        self.hash_google = url_google.url_hash

    def test_view_main_page(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_short_url(self):
        response = self.client.post('/create/', data={'url': 'https://test.ru'})
        self.assertTrue(response.context['messages'])

    def test_none_create_short_url(self):
        response = self.client.post('/create/', data={})
        self.assertFalse(response.context['messages'])

    def test_redirect_by_short_url(self):
        response = self.client.get(f'/{self.hash_google}/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_by_none_exist_short_url(self):
        response = self.client.get(f'/none_exist_url_hash/')
        self.assertEqual(response.status_code, 404)
