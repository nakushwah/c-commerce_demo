from django.test import TestCase
from accounts.models import User
from django.utils.timezone import now
from products.models import Product


class TestProduct(TestCase):
    @classmethod
    def setUpTestData(cls):
        """ Set up non-modified objects used by all test methods """
        user = User.objects.create(first_name='Big', last_name='Bob',
                                   email="one@gmail.com", username="bobby",
                                   password="one234five"
                                   )
        user.user_type = "User"
        user.contact = 6897564123
        user.contact2 = 1369875210
        user.is_verified = True
        user.updated_date = now()
        user.save()

        Product.objects.create(
            name="adidas_shoes", details="NA", price=1200,
            stocks=12, availability="Available", category="mobile",
            image1="image.png", image2="image.png", image3="image.png",
            Video="adidas_shoes",
        )

    def test_add_product(self):
        pr = Product.objects.all().first()
        product = Product.objects.create(
            name="adidas_shoes", details="NA", price=1200,
            stocks=12, availability="Available", category="mobile",
            image1="image.png", image2="image.png", image3="image.png",
            Video="adidas_shoes",
        )
        self.assertNotEqual(pr, product)

