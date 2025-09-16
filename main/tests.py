from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase): 
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'home.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Sepatu Burhan",
            price=150000,
            description="Sepatu keramat Burhan FC",
            thumbnail="https://example.com/sepatu.jpg",
            category="sport",
            is_featured=True
        )
        self.assertEqual(product.name, "Sepatu Burhan")
        self.assertEqual(product.price, 150000)
        self.assertTrue(product.is_featured)

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Kaos Panda BC",
            price=50000,
            description="Kaos official Panda BC",
            thumbnail="https://example.com/kaos.jpg",
            category="fashion"
        )
        # default is_featured harus False
        self.assertFalse(product.is_featured)
