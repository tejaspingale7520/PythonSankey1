from django.test import TestCase
from .models import CartItem

# Create your tests here.
class CartItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a school object for testing
        CartItem.objects.create(
            product_name='shirt',
            product_price=500.50,
            product_quantity=2
        )
    
    def test_CartItem_product_name(self):
        item = CartItem.objects.get(id=1)
        expected_name = 'shirt'
        self.assertEqual(item.product_name, expected_name)

    def test_CartItem_product_price(self):
        item = CartItem.objects.get(id=1)
        expected_price = 500.50
        self.assertEqual(item.product_price, expected_price)

    def test_CartItem_product_quantity(self):
        item = CartItem.objects.get(id=1)
        expected_quantity = 2
        self.assertEqual(item.product_quantity, expected_quantity)
