from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('apparel', 'Apparel'),
        ('active_wear', 'Active Wear'),
        ('footwear', 'Footwear'),
        ('equipments', 'Equipments'),
        ('nutrition_supplement', 'Nutrition & Supplement'),
        ('accessories', 'Accessories'),
        ('exclusive', 'Exclusive Items'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default = 'update')
    product_views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False) 

    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 25
    
    def increment_views(self):
        self.product_views += 1
        self.save()