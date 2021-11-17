from django.test import TestCase
from django.utils.timezone import now

from ..models import User, Address, Customer, Vendor


class TestUserModels(TestCase):
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

        Address.objects.create(user_id=user,
                               country="INDIA",
                               address="INDIA HINDUSTAN",
                               city="INDORE",
                               zipcode="452012",
                               )

        Customer.objects.create(user_id=user,
                                country="INDIA",
                                address="INDIA HINDUSTAN",
                                city="INDORE",
                                zipcode="452012",
                                landmark="near lapataganj"
                                )

        Vendor.objects.create(user_id=user,
                              country="INDIA",
                              address="INDIA HINDUSTAN",
                              city="INDORE",
                              zipcode="452012",
                              shop_name="vastubandar"
                              )

    def test_contact_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('contact').verbose_name
        self.assertEqual(field_label, 'Mobile Number')

    def test_get_user(self):
        user = User.objects.all().first()
        self.assertEqual(user.first_name, "Big")

    def test_get_customer(self):
        customer = Customer.objects.all().first()
        self.assertEqual(customer.user_id.first_name, "Big")

    def test_get_vendor(self):
        vendor = Vendor.objects.all().first()
        self.assertEqual(vendor.user_id.first_name, "Big")
