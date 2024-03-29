from django.db import models
from django.urls import reverse


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, default='-')

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='discount')
    PRICE = 1
    PERCENT = 2
    DISCOUNT_CHOICES = ((PRICE, 'قیمتی'), (PERCENT, 'درصدی'))
    status = models.IntegerField(choices=DISCOUNT_CHOICES, blank=True)
    amount = models.IntegerField()
    ACTIVE = 1
    INACTIVE = 2
    ACTIVE_CHOICES = ((ACTIVE, 'فعال'), (INACTIVE, 'غیرفعال'))
    is_active = models.IntegerField(choices=ACTIVE_CHOICES, blank=True)
    discount_limit = models.IntegerField()

    def __str__(self):
        return f'{self.name},{self.amount},{self.status}[0],{self.is_active}[0]'


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product/%Y%m')
    unavailable = 1
    available = 2
    STATUS_CHOICES = ((unavailable, 'ناموجود'), (available, 'موجود'))
    status = models.IntegerField(choices=STATUS_CHOICES, blank=True)
    description = models.TextField()
    discount = models.ManyToManyField(Discount, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.price}'

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug,])

    #
    # @price
    # def price(self):
    #     return self.price - self.discount
