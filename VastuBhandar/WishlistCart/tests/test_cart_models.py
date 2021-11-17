from django.test import TestCase
from accounts.models import User
from django.utils.timezone import now
from products.models import Product
from ..models import Wishlist, UserCart


class TestWishlist(TestCase):
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

        product = Product.objects.create(
            name="adidas_shoes", details="NA", price=1200,
            stocks=12, availability="Available", category="mobile",
            image1="image.png", image2="image.png", image3="image.png",
            Video="adidas_shoes",
        )

    def test_valid_add_wishlist(self):
        product_id = Product.objects.all().first()
        user = User.objects.all().first()
        wishlist = Wishlist.objects.create(user_id=user, product_id=product_id)
        self.assertEqual(wishlist.user_id, user)


    def test_valid_add_cart(self):
        product_id = Product.objects.all().first()
        user = User.objects.all().first()
        cart = UserCart.objects.create(user_id=user, product_id=product_id,
                                           quantity=22, cart_price=12000)
        self.assertEqual(cart.user_id, user)



