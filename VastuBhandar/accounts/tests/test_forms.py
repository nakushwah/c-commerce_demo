from django.test import TestCase
from ..forms import CreateUserForm


class TestCreateUserForm(TestCase):
    def test_user_create_form_valid(self):
        data = {
            "username": "buntu", "first_name": "anand",
            "last_name": "prapti", "email": "as@gmail.com",
            "user_type": "User",
            "password1": "jldsjfl@?/13", "contact": 1236547890,
            "contact2": 1236547890, "password2": "jldsjfl@?/13",
        }
        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_user_create_form_invalid(self):
        data = {
            "username": "buntu", "first_name": "anand",
            "last_name": "prapti", "email": "as@gmail.com",
            "user_type": "User",
            "password1": "one234", "contact": 1236547890,
            "contact2": 1236547890, "password2": "one234",
        }
        form = CreateUserForm(data=data)
        self.assertFalse(form.is_valid())
