from django.test import TestCase
from ..forms import ProductForms


class TestProductForms(TestCase):
    def test_form_invalid_data(self):
        data = {
            "name": "adidas shoes", "details": "anand",
            "price": 1200, "availability": "Available",
            "stocks": 12,
            "category": "mobile", "image1": "image.png",
            "image2": "image.png", "image3": "image.png",
            "image4": "image.png", "image5": "image.png",
            "Video": "image.png",
        }
        form = ProductForms(data=data)
        self.assertFalse(form.is_valid())