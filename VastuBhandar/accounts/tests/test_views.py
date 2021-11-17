from django.test import TestCase, RequestFactory

from ..models import User
from ..views import Register, Home
from django.urls import reverse


class TestHomePage(TestCase):
    def setUp(self):
        self.client = RequestFactory()
        self.home_url = reverse("home")
        self.register_url = reverse("Register")

        self.user = User.objects.create(first_name='Big', last_name='Bob',
                                        email="one@gmail.com", username="bobby",
                                        password="one234five"
                                        )

        self.form_user = {
            "username": "buntu", "first_name": "anand",
            "last_name": "prapti", "email": "as@gmail.com",
            "user_type": "User",
            "password1": "one234", "contact": 1236547890,
            "contact2": 1236547890, "password2": "one234",
        }

    def test_home_page(self):
        request = self.client.get(self.home_url)
        request.session = {}
        request.user = self.user
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        request = self.client.post(self.register_url, self.form_user)
        response = Register.as_view()(request)
        self.assertEqual(response.template_name[0], "account.html")

