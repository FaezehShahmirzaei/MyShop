from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, default='-')

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, default='-')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product_images/')
    unavailable = 1
    available = 2
    STATUS_CHOICES = ((unavailable, 'ناموجود'), (available, 'موجود'))
    status = models.IntegerField(choices=STATUS_CHOICES, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name, self.price}'
